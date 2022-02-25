from flask import Flask,render_template,request,flash, redirect
from src.linear_regression.lin_reg import Linear_regression
from src.logistic_regression.log_reg import Logistic_Regression

app=Flask("__name__")



@app.route("/linreg",methods=["POST","GET"])
def linreg():
    if request.method == "POST":
        CRIM=request.form.get("CRIM")
        ZN=request.form.get("ZN")
        INDUS=request.form.get("INDUS")
        CHAS=request.form.get("CHAS")
        NOX=request.form.get("NOX")
        RM=request.form.get("RM")
        AGE=request.form.get("AGE")
        DIS=request.form.get("DIS")
        RAD=request.form.get("RAD")
        TAX=request.form.get("TAX")
        PTRATIO=request.form.get("PTRATIO")
        B=request.form.get("B")
        LSTAT=request.form.get("LSTAT")
        inp={"CRIM":CRIM, "ZN":ZN,"INDUS":INDUS, "CHAS":CHAS,"NOX":NOX, "RM":RM, "AGE":AGE,"DIS" :DIS, "RAD":RAD, "TAX":TAX,"PTRATIO":PTRATIO, "B":B, "LSTAT":LSTAT}
        resp = Linear_regression().predict(inp)

        return render_template("linearregpred.html",result=resp)

    return render_template("linearregpred.html")




@app.route("/logreg",methods=["POST","GET"])
def logreg():
    if request.method == "POST":
        rate_marriage=request.form.get("rate_marriage")
        age=request.form.get("age")
        yrs_married=request.form.get("yrs_married")
        children=request.form.get("children")
        religious=request.form.get("religious")
        educ=request.form.get("educ")
        occupation=request.form.get("occupation")
        occupation_husb=request.form.get("occupation_husb")
        inp={"rate_marriage":rate_marriage, "age":age,"yrs_married":yrs_married, "children":children,"religious":religious, "educ":educ, "occupation":occupation,"occupation_husb" :occupation_husb}
        resp = Logistic_Regression().predict(inp)

        return render_template("logisticregpred.html",result=resp)

    return render_template("logisticregpred.html")

        
        











if __name__=="__main__":
    app.run()