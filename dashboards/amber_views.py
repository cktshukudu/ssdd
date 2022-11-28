from urllib import request
from django.shortcuts import render
from django.db import connection
from django.views import generic






def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ] 


def Economic_Amber(request):
    cursor = connection.cursor()
    cursor.execute("DECLARE @QUESTION1 NVARCHAR(MAX) = 'In addition to the grant, does the family have access to other sources of income?' \
                        DECLARE @QUESTION2 NVARCHAR(MAX) = 'Does your family have enough money to buy the things you need?' \
                        DECLARE @QUESTION3 NVARCHAR(MAX) = 'Do you struggle to pay off debts?' \
                        SELECT DISTINCT table_1.ID_Number, table_1.Name, table_1.Surname,table_1.Survey_ID, table_1.GPS_Location \
                        FROM \
                        (SELECT Survey.Survey_ID, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location  \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION1 AND Response = 'No' )) AS table_1 INNER JOIN \
                        (SELECT Survey.SurveyName, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location  \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION2 AND Response = 'Sometimes')) AS table_2 \
                        ON table_1.ID_Number = table_2.ID_Number INNER JOIN\
                        (SELECT Survey.SurveyName, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number\
                        FROM     Responses INNER JOIN\
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN\
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN\
                        Questions ON Responses.Question_ID = Questions.Question_ID\
                        WHERE (Question_Text = @QUESTION3 AND Response = 'Yes' )) AS table_3\
                         ON  table_1.ID_Number = table_3.ID_Number\
                        ORDER BY table_1.Name")
    rows = dictfetchall(cursor)  #Fetch the data from your db to be used by the program - use the fetchall() method
   # connection.close()
    return render(request, 'amber.html',{'data':rows}) 

def Education_Amber(request):
    cursor = connection.cursor()
    cursor.execute("DECLARE @QUESTION1 NVARCHAR(MAX) = 'Is your child progressing with their schoolwork?' \
                        DECLARE @QUESTION2 NVARCHAR(MAX) = 'Is the child afraid or refuses to go to school?' \
                        DECLARE @QUESTION3 NVARCHAR(MAX) = 'Does your child attend school on the days they are supposed to?'\
                        SELECT DISTINCT table_1.ID_Number, table_1.Name, table_1.Surname, table_1.Survey_ID \
                        FROM \
                        (SELECT Survey.Survey_ID, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location  \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION1 AND Response = 'No')) AS table_1 INNER JOIN \
                        (SELECT Survey.SurveyName, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location  \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION2 AND Response = 'Yes')) AS table_2 \
                        ON table_1.ID_Number = table_2.ID_Number INNER JOIN\
                        (SELECT Survey.SurveyName, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number\
                        FROM     Responses INNER JOIN\
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN\
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN\
                         Questions ON Responses.Question_ID = Questions.Question_ID\
                         WHERE (Question_Text = @QUESTION3 AND Response = 'NO' )) AS table_3\
                        ON  table_1.ID_Number = table_3.ID_Number\
                        ORDER BY table_1.Name")
    rows = dictfetchall(cursor)  #Fetch the data from your db to be used by the program - use the fetchall() method
   # connection.close()
    return render(request, 'amber.html',{'data':rows})

def Health_Amber(request):
    cursor = connection.cursor()
    cursor.execute("DECLARE @QUESTION1 NVARCHAR(MAX) = 'Is your childs health stopping him/her from playing/going to school?' \
                        DECLARE @QUESTION2 NVARCHAR(MAX) = 'Compared to other children, does your child struggle to hear, see or talk?' \
                        SELECT DISTINCT table_1.ID_Number, table_1.Name, table_1.Surname,table_1.Survey_ID, table_1.GPS_Location \
                        FROM \
                        (SELECT Survey.Survey_ID, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION1 AND Response = 'Sometimes' )) AS table_1 INNER JOIN \
                        (SELECT Survey.SurveyName, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location  \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION2 AND Response = 'Sometimes' )) AS table_2 \
                        ON table_1.ID_Number = table_2.ID_Number\
                        ORDER BY table_1.Name")
    rows = dictfetchall(cursor)  #Fetch the data from your db to be used by the program - use the fetchall() method
   # connection.close()
    return render(request, 'amber.html',{'data':rows})  



def Protection_Amber(request):
    cursor = connection.cursor()
    cursor.execute("    DECLARE @QUESTION1 NVARCHAR(MAX) = 'Has the child seen people that are fighting, swearing or hurting each other at home or in the community?' \
                        DECLARE @QUESTION2 NVARCHAR(MAX) = 'Has the child been a  victim of abuse or violence?' \
                        DECLARE @QUESTION3 NVARCHAR(MAX) = 'Is there an adult in the home that always knows where the child is?' \
                        SELECT DISTINCT table_1.ID_Number, table_1.Name, table_1.Surname,table_1.Survey_ID, table_1.GPS_Location \
                        FROM \
                        (SELECT Survey.Survey_ID, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION1 AND Response = 'Yes' )) AS table_1 INNER JOIN \
                        (SELECT Survey.SurveyName, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location  \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION2 AND Response = 'Sometimes')) AS table_2 \
                        ON table_1.ID_Number = table_2.ID_Number INNER JOIN\
                        (SELECT Survey.SurveyName, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number\
                        FROM     Responses INNER JOIN\
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN\
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN\
                        Questions ON Responses.Question_ID = Questions.Question_ID\
                        WHERE (Question_Text = @QUESTION3 AND Response = 'No' )) AS table_3\
                        ON  table_1.ID_Number = table_3.ID_Number\
                        ORDER BY table_1.Name")
    rows = dictfetchall(cursor)  #Fetch the data from your db to be used by the program - use the fetchall() method
   # connection.close()
    return render(request, 'amber.html',{'data':rows})   
  

def Nutrition_Amber(request):
    cursor = connection.cursor()
    cursor.execute("DECLARE @QUESTION1 NVARCHAR(MAX) = 'Does your child ever go to sleep hungry?' \
                        DECLARE @QUESTION2 NVARCHAR(MAX) = 'Is there enough food for your child to eat at every meal?' \
                        SELECT DISTINCT table_1.ID_Number, table_1.Name, table_1.Surname, table_1.GPS_Location \
                        FROM \
                        (SELECT Survey.SurveyName, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION1 AND Response = 'Sometimes' )) AS table_1 INNER JOIN \
                        (SELECT Survey.SurveyName, Questions.Question_Text, Responses.Response, Respondent.Name, Respondent.Surname, Respondent.ID_Number, Respondent.GPS_Location  \
                        FROM  Responses INNER JOIN \
                        Survey ON Responses.Survey_ID = Survey.Survey_ID INNER JOIN \
                        Respondent ON Responses.NewGUID = Respondent.NewGUID INNER JOIN \
                        Questions ON Responses.Question_ID = Questions.Question_ID \
                        WHERE (Question_Text = @QUESTION2 AND Response = 'Sometimes')) AS table_2 \
                        ON table_1.ID_Number = table_2.ID_Number\
                        ORDER BY table_1.Name")
    rows = dictfetchall(cursor)  #Fetch the data from your db to be used by the program - use the fetchall() method
   # connection.close()
    return render(request, 'amber.html',{'data':rows})   



