//var drop_subs=document.querySelector("#drop_subs");
//var new_row=document.createElement("tr");
//var new_data=document.createElement("td");
var select=document.querySelector("#lecture-module");
var dsubs=document.querySelector("#drop_subs");

/*
new_data.textContent="new_data1";

new_row.appendChild(new_data);

table1.appendChild(new_row);
*/

const m1=["sub1","sub2","sub3"];
const m2=["sub4","sub5","sub6"];
const m3=["sub7","sub8","sub9"];


function subs_select()
{
    
    var module1=select.options[select.selectedIndex].value;
    
    if(module1=="none")
        {
            dsubs.innerHTML="Please select a Module"
        }
    
     else if(module1=="M1")
      {    
        dsubs.innerHTML="";  
        for(i=0;i<m1.length;i++)
            {
                $("#drop_subs").append("<label class=lbl><input type=checkbox class=checkb>"+m1[i]+"</label>");
            }
       //   $("#drop_subs").append("<label><input type=checkbox name=checkAll id=checkAll>Select All</label>");
      }
    else if(module1=="M2")
      {    
        dsubs.innerHTML="";    
        for(i=0;i<m2.length;i++)
            {
                $("#drop_subs").append("<label class=lbl><input type=checkbox class=checkb>"+m2[i]+"</label>");
            }
      }
    else if(module1=="M3")
      {     
        dsubs.innerHTML="";    
        for(i=0;i<m3.length;i++)
            {
                $("#drop_subs").append("<label class=lbl><input type=checkbox class=checkb>"+m3[i]+"</label>");
            }
      }
}
  
function drop()
{
    $(".lbl").has("input:checked").remove();
}
                     