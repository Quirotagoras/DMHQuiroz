from django.shortcuts import render
from .forms import ExportXLSX
from receta.models import Receta
from django.http import HttpResponseRedirect,HttpResponse
from users.models import Capturista,Gerente
import io
from xlsxwriter.workbook import Workbook


def exportXLSXGerente(request,idEmpleado):
    if request.method == 'POST':
        form = ExportXLSX(request.POST)
        if form.is_valid():
            pk = request.user.pk
            user = Gerente.objects.get(user=pk)
            farmacia_id = user.farmacia
            fechaHasta=form.data['fechaHasta']

            fechaDesde = form.data['fechaDesde']#regresa datetime.datetime object
            nombreArchivo=form.data['nombreArchivo']

            recetas = Receta.objects.filter(creado__lte=fechaHasta, creado__gte=fechaDesde,farmacia_id=farmacia_id)


            output = io.BytesIO()
            ###XLSXWRITER#######

            workbook = Workbook(output, {'in_memory': True,'remove_timezone':True})

            worksheet = workbook.add_worksheet()
            worksheet.insert_image('W1', 'static/DMHQuiroz/logo.jpg',
                                   {'x_offset': 0, 'y_offset': 0, 'x_scale': .3, 'y_scale': .3})
            worksheet.set_column('I:I', 150)
            worksheet.set_column('N:N', 20)
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

            table = workbook.add_format({
                'font_size': '7',
                'align': 'center',

            })

            #####Header########
            worksheet.write('I9', 'Fecha de repecion para revision:___________________________', left_format)
            worksheet.write('I10', 'Referencia de CFDI:____________________________________', left_format)
            worksheet.merge_range('D4:G4', 'Formato 02', merge_format)
            worksheet.merge_range('D5:G5', 'Relacion de recetas surtidas', merge_format)
            worksheet.merge_range('A8:B8', 'Contrato:PMX-2018-61-330 SAP 46000006922', left_format)
            worksheet.merge_range('A7:B7', 'Localidad: ' + str(farmacia_id), left_format)
            worksheet.merge_range('A9:B9', 'Periodo: ' + fechaDesde+' - '+fechaHasta , left_format)
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
            date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})

            ######DATA#####
            importe_total=0
            iva_total=0

            for i in recetas:

                importe = i.cbarras.costo_venta*i.cantidad
                total=i.cbarras.iva+importe

                worksheet.write(row,col,i.folio_receta)
                worksheet.write(row, col+1, i.fecha_expide,date_format)
                worksheet.write(row, col + 2, i.doctor)
                worksheet.write(row, col + 3, i.ficha_derechohabiente.nombre)
                worksheet.write(row, col + 4, i.ficha_derechohabiente.ficha)
                worksheet.write(row, col + 5, i.ficha_derechohabiente.codigo)
                worksheet.write(row, col + 6, i.fecha_recibe,date_format)
                worksheet.write(row, col + 7, i.fecha_surte, date_format)
                worksheet.write(row, col + 8, str(i.cbarras))
                worksheet.write(row, col + 9, i.cantidad)
                worksheet.write(row, col + 10, '$'+str(i.cbarras.costo_venta))
                worksheet.write(row, col + 11, '$' + str(importe))#importe
                worksheet.write(row, col + 12,  '$'+str(i.cbarras.iva))
                worksheet.write(row, col + 13, '$'+str(total))

                importe_total+=total
                iva_total+=i.cbarras.iva
                row+=1

            worksheet.write(row,col+13,'$'+str(importe_total))
            worksheet.write(row, col + 12, '$'+str(iva_total))




            #####DATA######
            ######Tabla de registros#########

            #####Footer######
            row+=4
            worksheet.merge_range('A'+str(row)+':G'+str(row), 'Importe Total: ' + "$"+str(importe_total), left_format)


            #####Footer######

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
            pk = request.user.pk
            user = Capturista.objects.get(user=pk)
            farmacia_id = user.farmacia
            fechaHasta=form.data['fechaHasta']

            fechaDesde = form.data['fechaDesde']#regresa datetime.datetime object
            nombreArchivo=form.data['nombreArchivo']

            recetas = Receta.objects.filter(creado__lte=fechaHasta, creado__gte=fechaDesde,farmacia_id=farmacia_id)


            output = io.BytesIO()
            ###XLSXWRITER#######

            workbook = Workbook(output, {'in_memory': True,'remove_timezone':True})

            worksheet = workbook.add_worksheet()
            worksheet.insert_image('W1', 'static/DMHQuiroz/logo.jpg',
                                   {'x_offset': 0, 'y_offset': 0, 'x_scale': .3, 'y_scale': .3})
            worksheet.set_column('I:I', 150)
            worksheet.set_column('N:N', 20)
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

            table = workbook.add_format({
                'font_size': '7',
                'align': 'center',

            })

            #####Header########
            worksheet.write('I9', 'Fecha de repecion para revision:___________________________', left_format)
            worksheet.write('I10', 'Referencia de CFDI:____________________________________', left_format)
            worksheet.merge_range('D4:G4', 'Formato 02', merge_format)
            worksheet.merge_range('D5:G5', 'Relacion de recetas surtidas', merge_format)
            worksheet.merge_range('A8:B8', 'Contrato:PMX-2018-61-330 SAP 46000006922', left_format)
            worksheet.merge_range('A7:B7', 'Localidad: ' + str(farmacia_id), left_format)
            worksheet.merge_range('A9:B9', 'Periodo: ' + fechaDesde+' - '+fechaHasta , left_format)
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
            date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})

            ######DATA#####
            importe_total=0
            iva_total=0

            for i in recetas:

                importe = i.cbarras.costo_venta*i.cantidad
                total=i.cbarras.iva+importe

                worksheet.write(row,col,i.folio_receta)
                worksheet.write(row, col+1, i.fecha_expide,date_format)
                worksheet.write(row, col + 2, i.doctor)
                worksheet.write(row, col + 3, i.ficha_derechohabiente.nombre)
                worksheet.write(row, col + 4, i.ficha_derechohabiente.ficha)
                worksheet.write(row, col + 5, i.ficha_derechohabiente.codigo)
                worksheet.write(row, col + 6, i.fecha_recibe,date_format)
                worksheet.write(row, col + 7, i.fecha_surte, date_format)
                worksheet.write(row, col + 8, str(i.cbarras))
                worksheet.write(row, col + 9, i.cantidad)
                worksheet.write(row, col + 10, '$'+str(i.cbarras.costo_venta))
                worksheet.write(row, col + 11, '$' + str(importe))#importe
                worksheet.write(row, col + 12,  '$'+str(i.cbarras.iva))
                worksheet.write(row, col + 13, '$'+str(total))

                importe_total+=total
                iva_total+=i.cbarras.iva
                row+=1

            worksheet.write(row,col+13,'$'+str(importe_total))
            worksheet.write(row, col + 12, '$'+str(iva_total))




            #####DATA######
            ######Tabla de registros#########

            #####Footer######
            row+=4
            worksheet.merge_range('A'+str(row)+':G'+str(row), 'Importe Total: ' + "$"+str(importe_total), left_format)


            #####Footer######

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
    return render(request,'../templates/exportXLSX.html',context)







