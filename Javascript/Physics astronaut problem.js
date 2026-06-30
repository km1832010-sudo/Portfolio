var per1 = 0; // velocity of person 1 
var per2 = 0; // velocity of person 2 
var ball = 10; // Speed of the ball (mass = 1)
var total = 0; // Total number of throws

while (true) {
    // First quarter of the loop: per1 throws the ball
    var recoil = 0.2; // Recoil velocity for per1 
    per1 -= recoil; // per1 loses momentum due to recoil 
    total++; //increment 1 after the throw
    
    // Second quarter of the loop: per2 catches the ball
    var momentumTransfer2 = ball / 51; // Momentum transfer to per2
    per2 += momentumTransfer2; // per2 gains momentum 
   
    
    console.log("Throw: " + total);
    console.log("Velocity of per1: " + per1);
    console.log("Velocity of per2: " + per2);
    console.log("Speed of ball: " + ball);
    console.log("-------------------------------------------------------------");
    
    // Check if per1 has more momentum than the ball
    if (per1 < ball*-1) {
        console.log("Condition met: per1 < -ball");
        break;
    }

    // Check if per2 has more momentum than the ball
    if (per2 > ball) {
        console.log("Condition met: per2 > ball");
        break;
    }
    ball -= momentumTransfer2; // Ball loses speed
    

    // Third quarter of the loop: per2 throws the ball
    per2 += recoil; // per2 loses momentum due to recoil 
    total++;//increment 1 after the throw 

    // Fourth quarter of the loop: per1 catches the ball
    var momentumTransfer1 = ball / 51; // Momentum transfer to per1
    per1 -= momentumTransfer1; // per1 loses momentum 
   
        
    console.log("Throw: " + total);
    console.log("Momentum of per1: " + per1);
    console.log("Momentum of per2: " + per2);
    console.log("Speed of ball: " + ball);
    console.log("-------------------------------------------------------------");
    
    // Check if per2 has more momentum than the ball
    if (per2 > ball) {
        console.log("Termination Condition Met: per2 > ball");
        break;
    }

    // Check if per1 has more momentum than the ball
    if (per1 < ball*-1) {
        console.log("Termination Condition Met: per1 > ball");
        break;
    }
     ball -= momentumTransfer1; // Ball loses speed
}

main();