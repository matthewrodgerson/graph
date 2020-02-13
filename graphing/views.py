from django.shortcuts import render
import matplotlib.pyplot as plt, mpld3
from django.http import HttpResponse
import pandas as pd
import seaborn as sns
from tkinter import filedialog
from tkinter import *
from django.template import loader


# Create your views here.
def selection(request):
    template = loader.get_template('graphing/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def select_file(request):
    root = Tk()
    #root.withdraw()
    #window = Toplevel()
    root.filename =  filedialog.askopenfilename(parent=root, initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    template = loader.get_template('graphing/index.html')
    if root.filename != "":
        context = { 'file_chosen':root.filename, 'message':"File selected"}
    else:
        context = { }
    root.destroy()
    return HttpResponse(template.render(context,request))
    #return root.filename
    
def graph_file(request):  
    file_name = request.POST["file_name"]
    df = pd.read_csv(file_name)
    f, ax = plt.subplots(figsize=(15, 10))
    sns.set_palette("Spectral")
    ax = sns.barplot(data=df, x="country", y="loan_amount")
    return HttpResponse(mpld3.fig_to_html(f))