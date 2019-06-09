let students = [
    {name: 'Remy', cohort: 'Jan'},
    {name: 'Genevieve', cohort: 'March'},
    {name: 'Chuck', cohort: 'Jan'},
    {name: 'Osmund', cohort: 'June'},
    {name: 'Nikki', cohort: 'June'},
    {name: 'Boris', cohort: 'June'}
];

for (var i=0;i<students.length;i++){
    console.log('Name:' + students[i].name + ', Cohort: ' + students[i].cohort);
}

let users = {
    employees: [
        {'first_name':  'Miguel', 'last_name' : 'Jones'},
        {'first_name' : 'Ernie', 'last_name' : 'Bertson'},
        {'first_name' : 'Nora', 'last_name' : 'Lu'},
        {'first_name' : 'Sally', 'last_name' : 'Barkyoumb'}
    ],
    managers: [
       {'first_name' : 'Lillian', 'last_name' : 'Chambers'},
       {'first_name' : 'Gordon', 'last_name' : 'Poe'}
    ]
 };



const usersSeparated = function (objectArrays) {
    console.log('EMPLOYEES')
    let counter = 1;
    for (var key in objectArrays.employees){
        var employee = objectArrays.employees[key]
        console.log(counter + " - " + employee.last_name + ", " + employee.first_name + " - " + (employee.first_name.length + employee.last_name.length))
        counter++
    };
    console.log('MANAGERS')
    counter = 1;
    for (var key in objectArrays.managers){
        var manager = objectArrays.managers[key]
        console.log(counter + " - " + manager.last_name + ", " + manager.first_name + " - " + (manager.first_name.length + manager.last_name.length))
        counter++
    }
}