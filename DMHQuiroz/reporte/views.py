from django.shortcuts import render
from .forms import ExportXLSX
from receta.models import Receta
from django.http import HttpResponseRedirect,HttpResponse
from users.models import Capturista,Gerente
import io
from xlsxwriter.workbook import Workbook


def parseDate(date):
    parsed = date.split('-')
    info ={'year': parsed[0], 'month': parsed[1], 'day': parsed[2]}
    return info

def exportXLSXGerente(request,idEmpleado):
    if request.method == 'POST':
        form = ExportXLSX(request.POST)
        if form.is_valid():
            recetas = []
            pk = request.user.pk
            user = Gerente.objects.get(user=pk)
            farmacia_id = user.farmacia
            fechaHasta=form.data['fechaHasta']
            fechaDesde = form.data['fechaDesde']#regresa datetime.datetime object
            nombreArchivo=form.data['nombreArchivo']
            info = Receta.objects.filter(creado__lte=fechaHasta, creado__gte=fechaDesde, farmacia_id=farmacia_id)
            iva_status = 0
            if (request.POST.get("con_Iva") and not(request.POST.get("sin_Iva"))):
                for i in info:
                    cbarras = i.cbarras
                    if (cbarras.iva>0) :
                        recetas.append(i)
            elif (request.POST.get("sin_Iva") and not(request.POST.get("con_Iva"))):
                iva_status = 1
                for i in info:
                    cbarras = i.cbarras
                    if (cbarras.iva == 0):
                        recetas.append(i)
            elif(request.POST.get("sin_Iva") and request.POST.get("con_Iva")):
                iva_status = 2
                recetas = info
            print(recetas)
            output = io.BytesIO()
            ###XLSXWRITER#######

            workbook = Workbook(output, {'in_memory': True,'remove_timezone':True})

            worksheet = workbook.add_worksheet()
            worksheet.insert_image('W1', 'static/DMHQuiroz/logo.jpg',
                                   {'x_offset': 0, 'y_offset': 0, 'x_scale': .3, 'y_scale': .3})
            worksheet.set_column('I:I', 200)
            worksheet.set_column('D:D', 40)
            worksheet.set_column('N:N', 20)
            worksheet.set_column('K:K', 20)
            worksheet.set_column('L:L', 20)
            worksheet.set_column('M:M', 20)
            worksheet.set_column('C:C', 40)
            merge_format = workbook.add_format({
                'bold': 1,
                'align': 'center',
                'valign': 'vcenter',
                'font_size': '10'}
            )

            left_format = workbook.add_format({
                'bold': 1,
                'align': 'left',
                'valign': 'vcenter',
                'font_size': '10',
                'underline' : True}
            )
            left_format.set_border(1)

            table = workbook.add_format({
                'font_size': '7',
                'align': 'center',


            })
            table.set_border(1)

            dateFormat = workbook.add_format({
                'font_size': '7',
                'align': 'center',
                'num_format': 'dd/mm/yyyy'
            })
            dateFormat.set_border(1)


            IVA = workbook.add_format({
                'bold':1,
                'font_size': 15,
                'align' : 'center',
                'valign' : 'center'
            })
            IVA.set_border(1)



            #####Header########
            fechaDesde = parseDate(fechaDesde)
            anoDesde = fechaDesde['year']
            mesDesde = fechaDesde['month']
            dayDesde = fechaDesde['day']

            fechaHasta = parseDate(fechaHasta)
            anoHasta = fechaHasta['year']
            mesHasta = fechaHasta['month']
            dayHasta = fechaHasta['day']

            worksheet.write('C1', 'PROVEEDOR: ', left_format)
            worksheet.write('D1', 'DISTIBUIDORA MÉDICA Y HOSPITALARIA QUIROZ SA DE CV ')
            worksheet.write('C2', 'Para: ', left_format)
            worksheet.write('D2', 'PETRÓLEOS MEXICANOS')
            worksheet.merge_range('A8:B8', 'Contrato:PMX-2018-61-330 SAP 46000006922', left_format)
            worksheet.merge_range('A7:B7', 'Localidad: ' + str(farmacia_id), left_format)
            worksheet.merge_range('A9:B9', 'Periodo: ' + dayDesde+'/'+mesDesde+'/'+anoDesde +' al '+dayHasta+'/'+mesHasta+'/'+anoHasta , left_format)
            if (iva_status == 0):
                worksheet.write('B11:C11', 'CON IVA',IVA)
            elif(iva_status == 1):
                worksheet.write('B11:C11', 'SIN IVA',IVA)
            elif (iva_status == 2):
                worksheet.write('B11:C11', 'GENERAL', IVA)
            #####Header########

            ######Tabla de registros#########
            worksheet.add_table('A13:N13')
            worksheet.set_column('A:D', 18)
            worksheet.set_column('G:I', 22)

            worksheet.write('A13', 'Folio de Receta', table)
            worksheet.write('B13', 'Fecha de la receta', table)
            worksheet.write('C13', 'Medico que Expide', table)
            worksheet.write('D13', 'Nombre de Derecho Habiente', table)
            worksheet.write('E13', 'Ficha', table)
            worksheet.write('F13', 'Cod', table)
            worksheet.write('G13', 'Fecha de recepcion de receta medica', table)
            worksheet.write('H13', 'Fecha de entrega de medicamento', table)
            worksheet.write('I13', 'Nombre del medicamento', table)
            worksheet.write('J13', 'Cant', table)
            worksheet.write('K13', 'Precio', table)
            worksheet.write('L13', 'Importe', table)
            worksheet.write('M13', 'IVA', table)
            worksheet.write('N13', 'Total', table)


            row = 13
            col = 0


            ######DATA#####
            importe_total = 0
            iva_total = 0
            iva_producto=0
            productos_cantidad = 0
            total_neto = 0

            for i in recetas:

                importe = i.cbarras.costo_venta*i.cantidad


                worksheet.write(row,col,i.folio_receta,table)
                worksheet.write(row, col+1, i.fecha_expide,dateFormat)
                worksheet.write(row, col + 2, i.doctor,table)
                worksheet.write(row, col + 3, i.ficha_derechohabiente.nombre,table)
                worksheet.write(row, col + 4, i.ficha_derechohabiente.ficha,table)
                worksheet.write(row, col + 5, i.ficha_derechohabiente.codigo,table)
                worksheet.write(row, col + 6, i.fecha_recibe,dateFormat)
                worksheet.write(row, col + 7, i.fecha_surte, dateFormat)
                worksheet.write(row, col + 8, str(i.cbarras),table)
                worksheet.write(row, col + 9, i.cantidad,table)
                worksheet.write(row, col + 10, '$'+str(i.cbarras.costo_venta),table)
                worksheet.write(row, col + 11, '$' + str(importe),table)#importe
                if(i.cbarras.iva > 0):
                    iva_producto = importe * (i.cbarras.iva/100)
                    worksheet.write(row, col + 12,  '$' + str(importe * (i.cbarras.iva/100)),table)
                else:
                    worksheet.write(row, col + 12, '$0',table)

                total = importe + iva_producto
                worksheet.write(row, col + 13, '$'+str(total),table)
                total_neto += total

                importe_total += importe
                iva_total += iva_producto
                row += 1
                productos_cantidad += i.cantidad

            worksheet.write(row, col + 11, '$' + str(importe_total), left_format)
            worksheet.write(row, col + 12, '$' + str(iva_total), left_format)
            worksheet.write(row,col+13,'$'+str(total_neto), left_format)





            #####DATA######
            ######Tabla de registros#########

            #####Footer######
            row+=4
            worksheet.write('A'+str(row), 'Importe Total: ', left_format)
            worksheet.write('B' + str(row),"$" + str(total_neto), left_format)
            row += 1
            worksheet.write('A' + str(row), 'Total Productos: ',left_format)
            worksheet.write('B' + str(row), str(productos_cantidad), left_format)
            row+=1
            worksheet.write('A' + str(row), 'Total Recetas: ', left_format)
            worksheet.write('B' + str(row), str(recetas.__len__()), left_format)

            #####Footer######
            ####Auxiliar Tecnico ####
            row += 4
            worksheet.write('A' + str(row), 'Nombre proveedor: ', left_format)
            worksheet.write('B' + str(row), form.data['nombreProveedor'], table)
            worksheet.write('C' + str(row), 'Auxiliar Texnico: ', left_format)
            worksheet.write('D' + str(row), form.data['auxiliarTecnico'], table)

            row += 1
            worksheet.write('A' + str(row), 'Cargo: ', left_format)
            worksheet.write('B' + str(row), 'Gerente', table)
            worksheet.write('C' + str(row), 'Ficha: ', left_format)
            worksheet.write('D' + str(row), form.data['ficha'], table)

            row += 1
            worksheet.write('A' + str(row), 'Firma: ', left_format)
            worksheet.write('B' + str(row), '', table)
            worksheet.write('C' + str(row), 'Firma: ', left_format)
            worksheet.write('D' + str(row), '', table)

            row += 1
            worksheet.write('A' + str(row), 'Fecha: ', left_format)
            worksheet.write('B' + str(row),  dayDesde + '/' + mesDesde + '/' + anoDesde + ' al ' + dayHasta + '/' + mesHasta + '/' + anoHasta, table)
            worksheet.write('C' + str(row), 'Fecha: ', left_format)
            worksheet.write('D' + str(row), '', table)

            #########################

            workbook.close()
            ############export############
            output.seek(0)
            response = HttpResponse(output.read(),
                                    content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = "attachment; filename="+nombreArchivo+".xlsx"

            output.close()
            ############export############
            ###XLSXWRITER#######

            return response


    else:
        form = ExportXLSX()

    context={'form':form}
    return render(request,'../templates/exportXLSXGerente.html',context)





def exportXLSX(request,idEmpleado):
    if request.method == 'POST':
        form = ExportXLSX(request.POST)
        if form.is_valid():
            recetas = []
            pk = request.user.pk
            user = Capturista.objects.get(user=pk)
            farmacia_id = user.farmacia
            fechaHasta = form.data['fechaHasta']
            fechaDesde = form.data['fechaDesde']  # regresa datetime.datetime object
            nombreArchivo = form.data['nombreArchivo']
            info = Receta.objects.filter(creado__lte=fechaHasta, creado__gte=fechaDesde, farmacia_id=farmacia_id)
            iva_status = 0
            if (request.POST.get("con_Iva") and not (request.POST.get("sin_Iva"))):
                for i in info:
                    cbarras = i.cbarras
                    if (cbarras.iva > 0):
                        recetas.append(i)
            elif (request.POST.get("sin_Iva") and not (request.POST.get("con_Iva"))):
                iva_status = 1
                for i in info:
                    cbarras = i.cbarras
                    if (cbarras.iva == 0):
                        recetas.append(i)
            elif (request.POST.get("sin_Iva") and request.POST.get("con_Iva")):
                iva_status = 2
                recetas = info
            print(recetas)
            output = io.BytesIO()
            ###XLSXWRITER#######

            workbook = Workbook(output, {'in_memory': True, 'remove_timezone': True})

            worksheet = workbook.add_worksheet()
            worksheet.insert_image('W1', 'static/DMHQuiroz/logo.jpg',
                                   {'x_offset': 0, 'y_offset': 0, 'x_scale': .3, 'y_scale': .3})
            worksheet.set_column('I:I', 200)
            worksheet.set_column('D:D', 40)
            worksheet.set_column('N:N', 20)
            worksheet.set_column('K:K', 20)
            worksheet.set_column('L:L', 20)
            worksheet.set_column('M:M', 20)
            worksheet.set_column('C:C', 40)
            merge_format = workbook.add_format({
                'bold': 1,
                'align': 'center',
                'valign': 'vcenter',
                'font_size': '10'}
            )

            left_format = workbook.add_format({
                'bold': 1,
                'align': 'left',
                'valign': 'vcenter',
                'font_size': '10',
                'underline': True}
            )
            left_format.set_border(1)

            table = workbook.add_format({
                'font_size': '7',
                'align': 'center',

            })
            table.set_border(1)

            dateFormat = workbook.add_format({
                'font_size': '7',
                'align': 'center',
                'num_format': 'dd/mm/yyyy'
            })
            dateFormat.set_border(1)

            IVA = workbook.add_format({
                'bold': 1,
                'font_size': 15,
                'align': 'center',
                'valign': 'center'
            })
            IVA.set_border(1)

            #####Header########
            fechaDesde = parseDate(fechaDesde)
            anoDesde = fechaDesde['year']
            mesDesde = fechaDesde['month']
            dayDesde = fechaDesde['day']

            fechaHasta = parseDate(fechaHasta)
            anoHasta = fechaHasta['year']
            mesHasta = fechaHasta['month']
            dayHasta = fechaHasta['day']

            worksheet.write('C1', 'PROVEEDOR: ', left_format)
            worksheet.write('D1', 'DISTIBUIDORA MÉDICA Y HOSPITALARIA QUIROZ SA DE CV ')
            worksheet.write('C2', 'Para: ', left_format)
            worksheet.write('D2', 'PETRÓLEOS MEXICANOS')
            worksheet.merge_range('A8:B8', 'Contrato:PMX-2018-61-330 SAP 46000006922', left_format)
            worksheet.merge_range('A7:B7', 'Localidad: ' + str(farmacia_id), left_format)
            worksheet.merge_range('A9:B9',
                                  'Periodo: ' + dayDesde + '/' + mesDesde + '/' + anoDesde + ' al ' + dayHasta + '/' + mesHasta + '/' + anoHasta,
                                  left_format)
            if (iva_status == 0):
                worksheet.write('B11:C11', 'CON IVA', IVA)
            elif (iva_status == 1):
                worksheet.write('B11:C11', 'SIN IVA', IVA)
            elif (iva_status == 2):
                worksheet.write('B11:C11', 'GENERAL', IVA)
            #####Header########

            ######Tabla de registros#########
            worksheet.add_table('A13:N13')
            worksheet.set_column('A:D', 18)
            worksheet.set_column('G:I', 22)

            worksheet.write('A13', 'Folio de Receta', table)
            worksheet.write('B13', 'Fecha de la receta', table)
            worksheet.write('C13', 'Medico que Expide', table)
            worksheet.write('D13', 'Nombre de Derecho Habiente', table)
            worksheet.write('E13', 'Ficha', table)
            worksheet.write('F13', 'Cod', table)
            worksheet.write('G13', 'Fecha de recepcion de receta medica', table)
            worksheet.write('H13', 'Fecha de entrega de medicamento', table)
            worksheet.write('I13', 'Nombre del medicamento', table)
            worksheet.write('J13', 'Cant', table)
            worksheet.write('K13', 'Precio', table)
            worksheet.write('L13', 'Importe', table)
            worksheet.write('M13', 'IVA', table)
            worksheet.write('N13', 'Total', table)

            row = 13
            col = 0

            ######DATA#####
            importe_total = 0
            iva_total = 0
            iva_producto = 0
            productos_cantidad = 0
            total_neto = 0

            for i in recetas:

                importe = i.cbarras.costo_venta * i.cantidad

                worksheet.write(row, col, i.folio_receta, table)
                worksheet.write(row, col + 1, i.fecha_expide, dateFormat)
                worksheet.write(row, col + 2, i.doctor, table)
                worksheet.write(row, col + 3, i.ficha_derechohabiente.nombre, table)
                worksheet.write(row, col + 4, i.ficha_derechohabiente.ficha, table)
                worksheet.write(row, col + 5, i.ficha_derechohabiente.codigo, table)
                worksheet.write(row, col + 6, i.fecha_recibe, dateFormat)
                worksheet.write(row, col + 7, i.fecha_surte, dateFormat)
                worksheet.write(row, col + 8, str(i.cbarras), table)
                worksheet.write(row, col + 9, i.cantidad, table)
                worksheet.write(row, col + 10, '$' + str(i.cbarras.costo_venta), table)
                worksheet.write(row, col + 11, '$' + str(importe), table)  # importe
                if (i.cbarras.iva > 0):
                    iva_producto = importe * (i.cbarras.iva / 100)
                    worksheet.write(row, col + 12, '$' + str(importe * (i.cbarras.iva / 100)), table)
                else:
                    worksheet.write(row, col + 12, '$0', table)

                total = importe + iva_producto
                worksheet.write(row, col + 13, '$' + str(total), table)
                total_neto += total

                importe_total += importe
                iva_total += iva_producto
                row += 1
                productos_cantidad += i.cantidad

            worksheet.write(row, col + 11, '$' + str(importe_total), left_format)
            worksheet.write(row, col + 12, '$' + str(iva_total), left_format)
            worksheet.write(row, col + 13, '$' + str(total_neto), left_format)

            #####DATA######
            ######Tabla de registros#########

            #####Footer######
            row += 4
            worksheet.write('A' + str(row), 'Importe Total: ', left_format)
            worksheet.write('B' + str(row), "$" + str(total_neto), left_format)
            row += 1
            worksheet.write('A' + str(row), 'Total Productos: ', left_format)
            worksheet.write('B' + str(row), str(productos_cantidad), left_format)
            row += 1
            worksheet.write('A' + str(row), 'Total Recetas: ', left_format)
            worksheet.write('B' + str(row), str(recetas.__len__()), left_format)

            #####Footer######
            ####Auxiliar Tecnico ####
            row += 4
            worksheet.write('A' + str(row), 'Nombre proveedor: ', left_format)
            worksheet.write('B' + str(row), form.data['nombreProveedor'], table)
            worksheet.write('C' + str(row), 'Auxiliar Texnico: ', left_format)
            worksheet.write('D' + str(row), form.data['auxiliarTecnico'], table)

            row += 1
            worksheet.write('A' + str(row), 'Cargo: ', left_format)
            worksheet.write('B' + str(row), 'Capturista', table)
            worksheet.write('C' + str(row), 'Ficha: ', left_format)
            worksheet.write('D' + str(row), form.data['ficha'], table)

            row += 1
            worksheet.write('A' + str(row), 'Firma: ', left_format)
            worksheet.write('B' + str(row), '', table)
            worksheet.write('C' + str(row), 'Firma: ', left_format)
            worksheet.write('D' + str(row), '', table)

            row += 1
            worksheet.write('A' + str(row), 'Fecha: ', left_format)
            worksheet.write('B' + str(row),
                            dayDesde + '/' + mesDesde + '/' + anoDesde + ' al ' + dayHasta + '/' + mesHasta + '/' + anoHasta,
                            table)
            worksheet.write('C' + str(row), 'Fecha: ', left_format)
            worksheet.write('D' + str(row), '', table)

            #########################

            workbook.close()
            ############export############
            output.seek(0)
            response = HttpResponse(output.read(),
                                    content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            response['Content-Disposition'] = "attachment; filename=" + nombreArchivo + ".xlsx"

            output.close()
            ############export############
            ###XLSXWRITER#######

            return response


    else:
        form = ExportXLSX()

    context = {'form': form}
    return render(request, '../templates/exportXLSX.html', context)
