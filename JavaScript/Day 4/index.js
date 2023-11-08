





function caught_speeding(speed, is_birthday){
    if(is_birthday === true){
        speed = speed - 5;
    }
    
    if(speed <= 60){
        console.log(0);
    }else if( 61 <= speed <= 80){
            console.log(1)
        }else if(speed >= 81){
            console.log(2);
        }
}

caught_speeding(60,false);
caught_speeding(65,false);
caught_speeding(65,true);

console.log('I am in VS code')




/*
function luckySum(a,b,c){
    if(a===13){
        return 'Sorry, I cannot calculate 13';
    }else if(b===13){
        return a;
    }else if(c===13){
        return a+b;
    }else{
        return a+b+c;
    }
}
console.log(luckySum(1,2,3));
console.log(luckySum(1,2,13));
console.log(luckySum(1,13,3));
console.log(luckySum(13,2,3));


function stringTimes(str, n){
    while (n>0){
        console.log(str);
        n--;
    }
}
stringTimes('Hi',10);
stringTimes('Hi',3);
stringTimes('Hi',2);



function monkeyTrouble(aSmile, bSmile){
    if((aSmile === true && bSmile === true) || (aSmile === false && bSmile === false)){
        return true;
    }else{
        return false;
    }
}
console.log(monkeyTrouble(true,true));
console.log(monkeyTrouble(false,false));
console.log(monkeyTrouble(true,false));

//end of function

function sleepIn(weekday, vacation){
    if(weekday !== true || vacation === true){
        return true;
    }else{
    return false;
    }
}

console.log(sleepIn(false,false));
console.log(sleepIn(true,false));
console.log(sleepIn(false,true));

*/