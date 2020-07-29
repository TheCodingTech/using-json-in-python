import json

people_string = '''
{
  "people": [
    {
      "fname": "TheCoding",
      "sname": "Tech",
      "DOB": "06/08/2020",
      "email": "TheCodingTech@gmail.com" #not a real email
    },
    {
      "fname": "TheCoding",
      "sname": "Tech",
      "DOB": null,
      "email": null
    }
  ]
}
'''
data = json.loads(people_string)
print(data)

#or
 
for person in data['people']:
  print(person['fname'])
