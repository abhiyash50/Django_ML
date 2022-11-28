from django.shortcuts import render

from joblib import load
model = load('./savedModels/model.joblib')


def predictor(request):
    return render(request, 'index.html') 


def formInfo(request):
    sepal_lengh = request.GET['Sepal_lenght']
    Sepal_Width = request.GET['Sepal_Width']
    pedal_Lenth = request.GET['pedal_Lenth']
    pedal_Width = request.GET['pedal_Width']
    
    y_pred =  model.predict([[sepal_lengh, Sepal_Width, pedal_Lenth, pedal_Width]])
    if y_pred[0] == 0:
        y_pred = 'Setosa'
    elif y_pred[0] == 1:
        y_pred = 'Versicolor'
    else:
        y_pred = 'Verginica'
    return render(request, 'result.html', {'result' : y_pred})