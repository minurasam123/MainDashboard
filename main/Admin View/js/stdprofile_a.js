
function newStudent() {
          
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
    

    if((level.value == 'none' || membsh.value == 'none') || fName.value.length == 0 || lName.value.length == 0 || 
        cimaID.value.length == 0 || email.value.length == 0 || username.value.length == 0 || password.value.length == 0){
       msg.style.opacity="1";
       setTimeout(() => msg.style.opacity="0",1500);
        
    }else{

        var rowCount = table.rows.length;
        var row = table.insertRow(rowCount);

        row.insertCell(0).innerHTML= rowCount;
        row.insertCell(1).innerHTML= fName.value;
        row.insertCell(2).innerHTML= lName.value;
        row.insertCell(3).innerHTML= cimaID.value;
        row.insertCell(4).innerHTML= level.value;
        row.insertCell(5).innerHTML= username.value;
        row.insertCell(6).innerHTML= password.value;
        row.insertCell(7).innerHTML= '<input type="button" value = "Delete" onClick="deleteRow(this)">';
        // x=x+1

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
 
function deleteRow(obj) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("myTableData");
    table.deleteRow(index);
    
}





function btnCreate() {
    document.getElementById("stdprofile").style.display="none";
    document.getElementById("student-creation-form").style.display="block";
}