#####NIkit Prabodh########
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from system.analysis import disease, medicine,medicine_timelimit,medicineword_timelimit, diseaseword,medicineword, disease_timelimit,diseaseword_timelimit, prescription_analysis
import operator, datetime
from collections import OrderedDict


def graphindex(request):
   context = RequestContext(request)
   return render_to_response('graphindex.html', context)

def graphdisease(request ):
   # varName=request.GET.get('diseasename', '')
	#if varName == '':
	#	return render(request, 'unsuccessfulHack.html', {"error_msg": "Please specify a course"})
	diseasename = request.POST['diseaseinput']
	a=disease(diseasename)
	total =0
	for i in a:
		total = total + i
	avg = total/12
	#str1 = "fever"
	words = diseaseword()
	words_sorted_by_value = dict(sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	#words_sorted_by_value = OrderedDict(sorted(words.items(), key=lambda x: x[1], reverse=True))
	#b=dataAnalytics.getOverall(courseName)
	#print a, "b", b
	#print "hello"
	#print a
	#assert(False)
	return render(request, 'graphdisease.html', {"data": a,"avg":avg,"total":total,"data2": words_sorted_by_value,"data3":words,"disease": diseasename})


def graphmedicine(request ):
   # varName=request.GET.get('diseasename', '')
	#if varName == '':
	#	return render(request, 'unsuccessfulHack.html', {"error_msg": "Please specify a course"})
	medicinename = request.POST['medicineinput']
	a=medicine(medicinename)
	total =0
	for i in a:
		total = total + i
	avg = total/12
	
	words = medicineword()
	words_sorted_by_value = dict(sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	
	#b=dataAnalytics.getOverall(courseName)
	#print a, "b", b
	#print "hello"
	print (a)
	#assert(False)
	return render(request, 'graphmedicine.html', {"data": a,"avg":avg,"total":total,"data2": words_sorted_by_value,"data3": words,"medicine": medicinename})

def graphmedicine_timelimit(request):

	startdate = request.POST['startdatemed_input']
	enddate = request.POST['enddatemed_input']
	medicinename = request.POST['medicineinput']
	c=medicine_timelimit(medicinename,startdate,enddate)
	total =0
	for i in c:
		total = total + i
	avg = total/12
	
	words = medicineword_timelimit(startdate, enddate)
	words_sorted_by_value = dict(sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	
   # varName=request.GET.get('diseasename', '')
	#if varName == '':
	#	return render(request, 'unsuccessfulHack.html', {"error_msg": "Please specify a course"})
	
	
	
	#b=dataAnalytics.getOverall(courseName)
	#print a, "b", b
	#print "hello"
	
	#assert(False)
	return render(request, 'graphmedicine.html', {"data": c,"avg":avg,"total":total,"medicine": medicinename,"data2":words_sorted_by_value,"data3":words})

def diseasewordcloud(request):

	words = diseaseword()

	return render(request, 'diseasewordcloud.html', {"data": words})

def graphdisease_timelimit(request):
	startdate = request.POST['startdate_input']
	enddate = request.POST['enddate_input']
	diseasename = request.POST['diseaseinput']
	c=disease_timelimit(diseasename,startdate,enddate)
	total =0
	for i in c:
		total = total + i
	avg = total/12
	
	words = diseaseword_timelimit(startdate, enddate)
	words_sorted_by_value = dict(sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	

	print (c)
	return render(request,'graphdisease.html',{"data":c,"avg":avg,"total":total,"disease":diseasename, "data2":words_sorted_by_value,"data3":words})
def choosefunctionmed(request):
	startdate = request.POST['startdatemed_input']
	enddate = request.POST['enddatemed_input']

	try:
		datetime.datetime.strptime(startdate, '%Y-%m-%d')
		datetime.datetime.strptime(enddate, '%Y-%m-%d')
		return graphmedicine_timelimit(request)
		
	except ValueError:	
		#raise ValueError("Incorrect data format, should be YYYY-MM-DD")
		return graphmedicine(request)

def choosefunction(request):
	startdate = request.POST['startdate_input']
	enddate = request.POST['enddate_input']

	try:
		datetime.datetime.strptime(startdate, '%Y-%m-%d')
		datetime.datetime.strptime(enddate, '%Y-%m-%d')
		return graphdisease_timelimit(request)
		
	except ValueError:	
		#raise ValueError("Incorrect data format, should be YYYY-MM-DD")
		return graphdisease(request)




def graphfollowup(request):
	d = prescription_analysis()
	print (d)
	return render(request, 'graphfollowup.html',{"data":d})
#####end NIkit Prabodh########