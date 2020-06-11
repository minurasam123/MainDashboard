function categorising(){
this.lectureStore=[];
var keyLevel=dlecture-level.value;
var keySubject=lecture-subject.value;
var value=lecture-subject.value;
this.add=categorising(keyLevel,keySubject,value)
{
    if(keyLevel!=null&&KeySubject!=null&&value!=null){
        this.lectureStore.push({keyLevel:keyLevel,keySubject:keySubject,value:value});
        return this.lectureStore;
    
    }
    else if(keyLevel==null){
    print("Please select a level to upload lecture notes");
    }
    else{
        print("Please select subject")
    }
};

function findLecture( findlevel,findkey) 
{
var findlevel=my-level.value
 var findkey=box.value;
for(var i=0;i<lectureStore.length;i++){
    if(this.lectureStore[i].keyLevel==findlevel&& this.lectureStore[i].keySubject==findkey){
        return this.lectureStore[i].value;
    }
}
return this.lectureStore;
};
}
