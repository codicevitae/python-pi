let cx, cy;
let radius;
let ticks = 10;
let iteration = 0;
let manual = true;

function setup() {
    createCanvas(windowWidth, windowHeight);
    radius = height / 2 - 100;
    cx = windowWidth/2;
    cy = windowHeight/2;
 }

function getVector(index, total) {
    const angle = map(index % total, 0, total, 0, TWO_PI);
    const v = p5.Vector.fromAngle(angle + PI);
    v.mult(r);
    return v;
}

function draw() {
    frameRate(5);
    translate(width / 2, height / 2);
    stroke(155, 100, 200);
    strokeWeight(3);
    noFill();
    ellipse(0, 0, radius * 2);

    // draw the ticks
    stroke("purple");
    beginShape(POINTS);
    let tickNum = 0;
    strokeWeight(5);
    for (let a = 0; a < 360; a += 360/ticks) {
        let angle = radians(a);
        let x = cos(angle) * radius;
        let y = sin(angle) * radius;
        stroke("purple");
        vertex(x, y);
    }
    endShape(POINTS);

    // draw the labels
    fill("black");
    stroke("white")
    for (let a = 0; a < 360; a += 360/ticks) {
        let angle = radians(a);
        let x = cos(angle) * radius;
        let y = sin(angle) * radius;

        x = cos(angle) * (radius + 40);
        y = sin(angle) * (radius + 40);
        text(tickNum, x, y);
        tickNum++
      }

      // draw the connection
      stroke("purple")
      strokeWeight(1);
      let startPoint = iteration;
      let endPoint = (iteration * 2) % ticks;

      let x1 = cos(radians(360/ticks*startPoint)) * radius;
      let y1 = sin(radians(360/ticks*startPoint)) * radius;
    
      let x2 = cos(radians(360/ticks*endPoint)) * radius;
      let y2 = sin(radians(360/ticks*endPoint)) * radius;

      line(x1, y1, x2, y2);
      
      if (manual || iteration > 100 ) {
             noLoop();
      }
    
      iteration++;
}

function keyPressed() {
    redraw();
}