from django.shortcuts import render 
from .models import Products
from .models import Product_variations
from django.contrib import messages
import openpyxl
from datetime import datetime


def index(request):
    if "GET" == request.method:
        all_pro_data=Products.objects.all()
        all_var_data=Product_variations.objects.all()
        return render(request, 'new_index.html', {'all_pro_data':all_pro_data,'all_var_data':all_var_data})
    else:
        if'excel_file' in request.FILES:
            excel_file = request.FILES["excel_file"]
            if not excel_file.name.endswith("xlsx"):
                messages.info(request,'wrong format')
                return render(request,'index.html')

        # you may put validations here to check extension or file size
        

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]     
        
        

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                if(cell.value!=None):
                    row_data.append(str(cell.value))
            excel_data.append(row_data)
        
        a=Products.objects.values_list('Product_name')
        ans=[i[0] for i in list(set(a))]
        
        b=Products.objects.values_list('lowcost')
        i=excel_data[0].index('Product')
        
        for j in range(1,len(excel_data)):
            if(excel_data[j][i] in ans):
                p_id=Products.objects.filter(Product_name=excel_data[j][i]).values('id')
                
                var_text=Product_variations.objects.filter(prodct_id=p_id[0]['id']).values('variation')

                if(len(var_text)!=0 and excel_data[j][1]==var_text[0]['variation']):
                    Product_variations.objects.filter(prodct_id=p_id[0]['id'],variation=var_text[0]['variation']).update(stock=excel_data[j][2])
                else:
                    p_data=Product_variations(
                        prodct_id=p_id,
                        variation=excel_data[j][1],
                        stock=excel_data[j][2],
                        last_update=datetime.now()
                    )
                    p_data.save()


            else:
                data=Products(
                    Product_name=excel_data[j][i],
                    lowcost=0,
                    last_update=datetime.now()
                )
                data.save()
                pro_id=Products.objects.filter(Product_name=excel_data[j][i]).values('id')
                p_data=Product_variations(
                        prodct_id=pro_id[0]['id'],
                        variation=excel_data[j][1],
                        stock=excel_data[j][2],
                        last_update=datetime.now()
                    )
                p_data.save()
        all_pro_data=Products.objects.all()
        all_var_data=Product_variations.objects.all()

        return render(request, 'new_index.html', {"excel_data":excel_data,'all_pro_data':all_pro_data,'all_var_data':all_var_data})
def test(request):
    return render(request,'index.html')

        
