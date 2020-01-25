let r;
let factor = 0;
let manual = true;
let incr = 1;

function setup() {
    createCanvas(windowWidth, windowHeight);
    r = height / 2 - 16;
}

function getVector(index, total) {
    const angle = map(index % total, 0, total, 0, TWO_PI);
    const v = p5.Vector.fromAngle(angle + PI);
    v.mult(r);
    return v;
}

function draw() {
    background(0);
    const total = 200;
    factor += incr;

    translate(width / 2, height / 2);
    stroke(155, 100, 200);
    strokeWeight(2);
    noFill();
    ellipse(0, 0, r * 2);

    strokeWeight(2);
    for (let i = 0; i < total; i++) {
        const a = getVector(i, total);
        const b = getVector(i * factor, total);
        line(a.x, a.y, b.x, b.y);
    }

    frameRate(10);

    if (manual) {
        noLoop();
    }

    stroke("white");
    text(factor, 500, 30);
}

function keyPressed() {
    
    if (key == "ArrowLeft") {
       factor = factor - 2;
    }

    redraw();
}