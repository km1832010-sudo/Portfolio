function main(){
    var num=2;
    var check=1;
    var count=2;
    while(true){
        while (count<20){
            if (check%num==0){
                count++;
                num++;
            }else{
                num=2;
                count=0;
                check++
            }
        }
        console.log(check);
        break;
    }
}
main();
