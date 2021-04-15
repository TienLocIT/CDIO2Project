function addnewRow(f){
    for(var i=1;i<7;i++){
        if(document.getElementById("skill"+i).style.display=="none"){
            document.getElementById("skill"+i).style.display="";
            return;
        }
    }
}