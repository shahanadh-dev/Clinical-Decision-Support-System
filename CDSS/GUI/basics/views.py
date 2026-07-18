from django.shortcuts import render, HttpResponse, redirect
from .models import *
import math
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = User.objects.filter(username=username)
        user = authenticate(request, username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('COPD')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


@login_required(login_url='login')
def COPD(request):
    if request.method == "POST":
        data = request.POST

        AGE = data.get("textfirstnumber")
        if AGE:  # Check if AGE is not empty
            AGE = int(AGE)
        else:
            AGE = 0  # Set a default value if input is missing

        PackHistory = float(data.get("texttwonumber"))
        FEV1PRED = float(data.get("textthirdnumber"))
        FVC = float(data.get("textfourthnumber"))
        FVCPRED = int(data.get("textfivenumber"))
        CAT = int(data.get("textsixnumber"))
        HAD = float(data.get("textsevennumber"))
        SGRQ = float(data.get("texteightnumber"))
        AGEquartiles = int(data.get("textninenumber"))
        copd = int(data.get("texttennumber"))
        gender = int(data.get("textelvennumber"))
        smoking = int(data.get("texttwelvenumber"))
        Diabetes = int(data.get("textthirteennumber"))
        muscular = int(data.get("textfourteennumber"))
        hypertension = int(data.get("textfifteenhnumber"))
        AtrialFib = int(data.get("textsixteennumber"))
        IHD = int(data.get("textseventeennumber"))

        if "buttonsubmitsvm" in request.POST:
            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.preprocessing import StandardScaler
            from sklearn.svm import SVC
            from sklearn.metrics import confusion_matrix

            data_path = r"C:\Users\shaha\Desktop\Project-COPD\Model-COPD\GUI\basics\Data\dataset.csv"
            data = pd.read_csv(data_path)

            columns_to_drop = ['Unnamed: 0', 'ID', 'MWT1', 'MWT2']
            data.drop(columns=columns_to_drop, inplace=True)

            inputs = data.drop(['COPDSEVERITY', 'MWT1Best', 'FEV1'], axis=1)
            output = data[['copd']]  # Keep 'copd' as a DataFrame

            x_train, x_test, y_train, y_test = train_test_split(inputs, output, test_size=0.2)

            sc = StandardScaler()
            x_train = sc.fit_transform(x_train)
            x_test = sc.transform(x_test)

            model = SVC()
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)

            cm = confusion_matrix(y_test, y_pred)
            acc = cm.trace() / cm.sum()  # Proper method to compute accuracy

            print(acc)
            result = model.predict([[AGE, PackHistory, FEV1PRED, FVC, FVCPRED, CAT, HAD, SGRQ,
                                     AGEquartiles, copd, gender, smoking, Diabetes, muscular,
                                     hypertension, AtrialFib, IHD]])

            return render(request, "MMA.html", context={
                "result": f"Result of SVM = {result}",
                "acc": f"Accuracy of SVM = {math.ceil(acc * 100)}%"
            })

        if "buttonsubmitknn" in request.POST:
            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.neighbors import KNeighborsClassifier
            from sklearn.metrics import confusion_matrix

            data_path = r"C:\Users\shaha\Desktop\Project-COPD\Model-COPD\GUI\basics\Data\dataset.csv"
            data = pd.read_csv(data_path)

            columns_to_drop = ['Unnamed: 0', 'ID', 'MWT1', 'MWT2']
            data.drop(columns=columns_to_drop, inplace=True)

            inputs = data.drop(['COPDSEVERITY', 'MWT1Best', 'FEV1'], axis=1)
            output = data[['copd']]  # Keep 'copd' as a DataFrame

            x_train, x_test, y_train, y_test = train_test_split(inputs, output, test_size=0.2)

            model = KNeighborsClassifier(n_neighbors=11)
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)

            cm = confusion_matrix(y_test, y_pred)
            acc = cm.trace() / cm.sum()  # Proper method to compute accuracy

            print(acc)
            result = model.predict([[AGE, PackHistory, FEV1PRED, FVC, FVCPRED, CAT, HAD, SGRQ,
                                     AGEquartiles, copd, gender, smoking, Diabetes, muscular,
                                     hypertension, AtrialFib, IHD]])

            return render(request, "MMA.html", context={
                "result": f"Result of KNN = {result}",
                "acc": f"Accuracy of KNN = {math.ceil(acc * 100)}%"
            })

    return render(request, "MMA.html")


def LogoutPage(request):
    logout(request)
    return redirect('login')