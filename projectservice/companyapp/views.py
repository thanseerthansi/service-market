from projectservice.globalimport import *

# Create your views here.
class Companyview(ListAPIView):#2 many 2 many ofields are......
    serializer_class = GetCompanySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)
    def post(self,request):
        id = self.request.POST.get("id",'')
        try:
            if id:
                if id.isdigit():
                    company_qs = CompanyModel.objects.filter(id=id)  
                    if company_qs.count():
                        company_obj = CompanySerializer(company_qs[0],data=self.request.data,partial=True)
                        msg = "updated successfully"
                    else:return  Response({"Status":status.HTTP_404_NOT_FOUND,"Messsage":"No Records found with given id"})
                else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"provide valid id"})
            else: 
                company_obj = CompanySerializer(data=self.request.data,partial=True)
                msg = "Created successfully"
            company_obj.is_valid(raise_exception=True)
            saved_data = company_obj.save()
            data_city = self.request.POST.get('cities','')
            if data_city :#to add  multiple city datas to many2many
                k=[]
                datac=json.loads(data_city)
                for i in datac:
                    city = ServiceCitiesModel.objects.filter(id=i)
                    if city.count:
                        city_qs = city.first()
                        k.append(city_qs)
                    else : return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id's"})
                saved_data.cities.add(*k)
            data_service = self.request.POST.get('services')
            if data_service : #to add  multiple service datas to many2many
                S=[]
                datas=json.loads(data_service)
                for i in datas:
                    service = ServiceModel.objects.filter(id=i)
                    if service.count:
                        service_qs = service.first()
                        S.append(service_qs)
                    else : return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id's"})
                saved_data.cities.add(*S)
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})
    def get_queryset(self):
        try:
            id = self.request.GET.get("id",'')
            cities = self.request.GET.get("cities")
            qs = CompanyModel.objects.all()
            if id : qs = qs.filter(id=id)
            if cities: qs = qs.filter(cities__in = cities)
            return qs
        except :return None
    def delete(self,request):
        id = self.request.data['id']
        try:
            qs = CompanyModel.objects.filter(id=id)
            if qs.count():
                qs = qs.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"deleted successfully"})
            return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No record found"})
        except Exception as e:
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})