import joblib
model = joblib.load('housemodel.pk1')
income = 80000
house_age = 3
room = 8
bed_room = 4
population  =23086.800503
m = model.predict([[income , house_age , room , bed_room , population]])
print(str(m[0]))