from projectservice.globalimport import *


# Create your views here.
class ServiceTypeVew(ListAPIView):
    serializer_class = ServiceTypeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)
    def post(self,request):
        if self.request.user.id != None :
            isadmin = self.request.user.is_admin
            superuser = self.request.user.is_superuser
            if isadmin==True or superuser == True  :
                try:
                    mandatory = ['service']
                    data = Validate(self.request.data,mandatory)
                    id = self.request.POST.get("id","")                     
                    if id: 
                        if id.isdigit():
                            service_type_qs = ServiceTypeModel.objects.filter(id=id)
                            if service_type_qs.count():
                                service_type_qs = service_type_qs.first()
                                service_type_obj = ServiceTypeSerializer(service_type_qs,data=self.request.data,partial=True)
                                msg = "Successfully modified"
                            else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
                        else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id"}) 
                    else: 
                        if data == True:
                            service_type_obj = ServiceTypeSerializer(data=self.request.data,partial=True)
                            msg = "Successfully Created" 
                        else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":data})          
                    service_type_obj.is_valid(raise_exception=True)
                    service_type_obj.save()
                    
                    return Response({"Status":status.HTTP_200_OK,"Message":msg})                
                except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})
            else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Something Went Wrong"})
        else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Need to login"})
    def get_queryset(self):
        try:
            id = self.request.GET.get("id",'')
            qs = ServiceTypeModel.objects.all()
            if id : qs = qs.filter(id=id)
            return qs.order_by('-id')
        except :return None
 
    def delete(self,request):
        if self.request.user.id != None :
            isadmin = self.request.user.is_admin
            superuser = self.request.user.is_superuser
            if isadmin == True or superuser == True :
                try:
                    id = self.request.data['id']
                    # id = json.loads(id)
                    objects = ServiceTypeModel.objects.filter(id=id)
                    if objects.count():
                        objects.delete()
                        return Response({"Status":status.HTTP_200_OK,"Message":"deleted successfully"})
                    else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No records with given id" })
                except Exception as e:
                    return Response({
                        "Status" : status.HTTP_400_BAD_REQUEST,
                        "Message" : str(e),
                    })
            else:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : "Something Went Wrong"
                })
        else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Need to login"})


class ServicecitiesVew(ListAPIView):
    serializer_class = ServiceCitiesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)
    def post(self,request):
        if self.request.user.id != None :
            isadmin = self.request.user.is_admin
            superuser = self.request.user.is_superuser
            if isadmin==True or superuser == True  :
                try:
                    mandatory = ['city','country']
                    data = Validate(self.request.data,mandatory)
                    id = self.request.POST.get("id","")                     
                    if id: 
                        if id.isdigit():
                            service_city_qs = ServiceCitiesModel.objects.filter(id=id)
                            if service_city_qs.count():
                                service_city_qs = service_city_qs.first()
                                service_city_obj = ServiceCitiesSerializer(service_city_qs,data=self.request.data,partial=True)
                                msg = "Successfully modified"
                            else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
                        else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id"}) 
                    else: 
                        if data == True:
                            service_city_obj = ServiceCitiesSerializer(data=self.request.data,partial=True)
                            msg = "Successfully Created" 
                        else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":data})          
                    service_city_obj.is_valid(raise_exception=True)
                    service_city_obj.save()
                    
                    return Response({"Status":status.HTTP_200_OK,"Message":msg})                
                except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})
            else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Something Went Wrong"})
        else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Need to login"})
    def get_queryset(self):
        try:
            id = self.request.GET.get("id",'')
            qs = ServiceCitiesModel.objects.all()
            if id : qs = qs.filter(id=id)
            return qs.order_by('-id')
        except :return None
 
    def delete(self,request):
        if self.request.user.id != None :
            isadmin = self.request.user.is_admin
            superuser = self.request.user.is_superuser
            if isadmin == True or superuser == True :
                try:
                    id = self.request.data['id']
                    # id = json.loads(id)
                    objects = ServiceCitiesModel.objects.filter(id=id)
                    if objects.count():
                        objects.delete()
                        return Response({"Status":status.HTTP_200_OK,"Message":"deleted successfully"})
                    else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No records with given id" })
                except Exception as e:
                    return Response({
                        "Status" : status.HTTP_400_BAD_REQUEST,
                        "Message" : str(e),
                    })
            else:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : "Something Went Wrong"
                })
        else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Need to login"})


#service
class ServiceVew(ListAPIView):
    serializer_class = ServiceSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)
    def post(self,request):
        if self.request.user.id != None :
            isadmin = self.request.user.is_admin
            superuser = self.request.user.is_superuser
            if isadmin==True or superuser == True  :
                try:
                    mandatory = ['service_type','service_name']
                    data = Validate(self.request.data,mandatory)
                    id = self.request.POST.get("id","")  
                    service_type = self.request.POST.get("service_type",'')
                    if service_type : 
                        service_type_qs = ServiceTypeModel.objects.filter(id=service_type)   
                        if service_type_qs.count(): service_type_obj = service_type_qs.first()
                        else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Service type not found with given id "})               
                    if id: 
                        if id.isdigit():
                            service_qs = ServiceModel.objects.filter(id=id)
                            if service_qs.count():
                                service_qs = service_qs.first()
                                if not service_type: service_type_obj = service_qs.service_type
                                service_obj = ServiceSerializer(service_qs,data=self.request.data,partial=True)
                                msg = "Successfully modified"
                            else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
                        else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id"}) 
                    else: 
                        if data == True:
                            service_obj = ServiceSerializer(data=self.request.data,partial=True)
                            msg = "Successfully Created" 
                        else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":data})          
                    service_obj.is_valid(raise_exception=True)
                    service_obj.save()
                    
                    return Response({"Status":status.HTTP_200_OK,"Message":msg})                
                except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})
            else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Something Went Wrong"})
        else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Need to login"})    
    def get_queryset(self):
        try:
            id = self.request.GET.get("id",'')
            service_type = self.request.GET.get("service_type",'')
            service_type_name = self.request.GET.get("servicetype_name",'')
            city = self.request.GET.get('city','')
            qs = ServiceModel.objects.all()
            if service_type: qs = qs.filter(service_type__id = service_type)
            if service_type_name: qs = qs.filter(service_type__service = service_type_name)
            if city : qs = qs.filter(city=city)
            if id : qs = qs.filter(id=id)
            return qs.order_by('-id')
        except :return None
 
    def delete(self,request):
        if self.request.user.id != None : 
            isadmin = self.request.user.is_admin
            superuser = self.request.user.is_superuser
            if isadmin == True or superuser == True :
                try:
                    id = self.request.data['id']
                    # id = json.loads(id)
                    objects = ServiceModel.objects.filter(id=id)
                    if objects.count():
                        objects.delete()
                        return Response({"Status":status.HTTP_200_OK,"Message":"deleted successfully"})
                    else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No records with given id" })
                except Exception as e:
                    return Response({
                        "Status" : status.HTTP_400_BAD_REQUEST,
                        "Message" : str(e),
                    })
            else:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : "Something Went Wrong"
                })
        else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Need to login"})

    def patch(self,request):    
        # if self.request.user.id != None : 
        #     isadmin = self.request.user.is_admin
        #     superuser = self.request.user.is_superuser
        #     if isadmin == True or superuser == True :  
        try:
            serviceid = self.request.POST['id']
            city = self.request.POST['city']
            keyword = self.request.POST['keyword']
            if city:
                city = json.loads(city)
                for i in city:
                    k=[]
                    city_qs = ServiceCitiesModel.objects.filter(id=i)
                    if city_qs.count():
                        city_qs = city_qs.first()
                        k.append(city_qs)
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Recoreds found with given id"})

            if serviceid :
                service_qs = ServiceModel.objects.filter(id=serviceid)
                if service_qs.count():
                    service_qs = service_qs.first()             
                else: 
                    return Response({"status":status.HTTP_404_NOT_FOUND,"message":"property not found"})
                if keyword=="add":           
                    service_qs.city.add(*k)
                    msg = "type added successfully"
                if keyword=="remove":
                    service_city = service_qs.city.all()
                    if city_qs not in service_city:return Response({status.HTTP_404_NOT_FOUND:False,"Message":"property not found in liked properties"})
                    else:
                        service_qs.city.remove(*k)
                        msg = "type removed successfully"
                return Response({
                    "status":status.HTTP_200_OK,
                    "message":msg,
                })
            else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"You Need to Login "})
        except Exception as e:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"msg": str(e),})
            # else:
            #     return Response({
            #         "Status" : status.HTTP_400_BAD_REQUEST,
            #         "Message" : "Something Went Wrong"
            #     })
        # else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Need to login"})