var fName = document.getElementById("inputfname");
var lName = document.getElementById("inputlname");
var cimaID = document.getElementById("inputID");
var level = document.getElementById("level");
var membsh = document.getElementById("membsh");
var email = document.getElementById("inputEmail");
var username = document.getElementById("inputUsername");
var password = document.getElementById("inputPW");
const msg = document.getElementById("msg");
var table = document.getElementById("myTableData"); 

var students=new Array();

showStudents();

function addStudents() { 
   
     if((level.value == 'none' || membsh.value == 'none') || fName.value.length == 0 || lName.value.length == 0 || 
        cimaID.value.length == 0 || email.value.length == 0 || username.value.length == 0 || password.value.length == 0){
        msg.style.opacity="1";
        setTimeout(() => msg.style.opacity="0",1500);    
     }else{
        getStudents();
        
        let student = {
            First_Name: fName.value,
            Last_Name: lName.value,
            CIMA_ID: cimaID.value,
            Level: level.value,
            Username: username.value,
            Password: password.value
        }
        students.push(student);
        localStorage.setItem("SavedProfiles",JSON.stringify(students));
        showStudents();

        level.value='none';
        membsh.value='none';
        fName.value="";
        lName.value="";
        cimaID.value="";
        email.value="";
        username.value="";
        password.value="";

        document.getElementById("stdprofile").style.display="block";
        document.getElementById("student-creation-form").style.display="none";  
    }
}

function getStudents() {
    var std = localStorage.getItem("SavedProfiles");
    if(std != null){
        students=JSON.parse(std);
    }
}


function showStudents(){
    getStudents();

    var x=table.rows.length;
    while(--x){
        table.deleteRow(x);
    }

    for( i=0 ; i<students.length ; i++){
        table.insertRow().innerHTML="<td>"+(i+1)+"</td>"+
                    "<td>"+students[i].First_Name+"</td>"+
                    "<td>"+students[i].Last_Name+"</td>"+
                    "<td>"+students[i].CIMA_ID+"</td>"+
                    "<td>"+students[i].Level+"</td>"+
                    "<td>"+students[i].Username+"</td>"+
                    "<td>"+students[i].Password+"</td>"+
                    "<td>"+'<input type="button" value = "Delete" onClick="deleteRow(this);">'+"</td>";
    }
}


// Complex way to show student profile details...
// function showStudents(){

//     var rowCount = table.rows.length;
//     getStudents();

//     var x=table.rows.length;
//      while(--x){
//            table.deleteRow(x);
//      }


//     for( i=0;i<students.length;i++){
//         var nrow = table.insertRow();
//         var ncell0 = nrow.insertCell();
//         var ncell1 = nrow.insertCell();
//         var ncell2 = nrow.insertCell();
//         var ncell3 = nrow.insertCell();
//         var ncell4 = nrow.insertCell();
//         var ncell5 = nrow.insertCell();
//         var ncell6 = nrow.insertCell();
//         var ncell7 = nrow.insertCell();

//         ncell0.innerHTML= (i+1);
//         ncell1.innerHTML= students[i].First_Name;
//         ncell2.innerHTML= students[i].Last_Name;
//         ncell3.innerHTML= students[i].CIMA_ID;
//         ncell4.innerHTML= students[i].Level;
//         ncell5.innerHTML= students[i].Username;
//         ncell6.innerHTML= students[i].Password;
//         ncell7.innerHTML= '<input type="button" value = "Delete" onClick="deleteRow(this);">';
//         }
// }

 
function deleteRow(obj) {

    var index = obj.parentNode.parentNode.rowIndex;
    alert("You Request to Delete "+students[index-1].First_Name);
    getStudents();
    table.deleteRow(index);

    students=students.slice(0,index-1).concat(students.slice(index,students.length));
    localStorage.setItem("SavedProfiles",JSON.stringify(students));
    showStudents();
}




function btnCreate() {
    document.getElementById("stdprofile").style.display="none";
    document.getElementById("student-creation-form").style.display="block";
}