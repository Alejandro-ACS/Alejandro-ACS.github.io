let time = 0;
let x = [];
let path = [];
let X;
let control = 0;

function windowResized(){
  resizeCanvas(windowWidth, windowHeight);
}

function setup() {
  createCanvas(windowWidth, windowHeight);
}

function mouseReleased(){
  control = 2;
  for (let i = 0; i < x.length; i++){
    x[i] = [x[i].x, x[i].y];
  }
  X = dft(x);
}

function mousePressed(){
  control = 1;
  x=[];
  time=0;
  path=[];
}

function epicycles(x, y, rotation, fourier) {
  for (let i = 0; i < fourier.length; i++) {
    let prevx = x;
    let prevy = y;
    let freq = fourier[i].freq;
    let radius = fourier[i].amp;
    let phase = fourier[i].phase;
    x += radius * cos(freq * time + phase + rotation);
    y += radius * sin(freq * time + phase + rotation);

    stroke(0, 50);
    noFill();
    ellipse(prevx, prevy, radius * 2);
    stroke(0, 75);
    line(prevx, prevy, x, y);
  }
  return createVector(x, y);
}

function draw() {
  if (control == 1){
    background(255);
    let point = createVector(mouseX - width / 2, mouseY - height / 2);
    x.push(point);
    beginShape();
    noFill();
    strokeWeight(2);
    stroke(0, 0, 0);
    for (let coord of x) {
      vertex(coord.x + width / 2, coord.y + height / 2);
    }
    endShape();
  } else if (control == 2){
    background(255);
    let v = epicycles(width / 2, height / 2, 0, X);
    path.unshift(v);
    beginShape();
    noFill();
    strokeWeight(2);
    stroke(0, 0, 0);
    for (let i = 0; i < path.length; i++) {
      vertex(path[i].x, path[i].y);
    }
    endShape();

    const dt = TWO_PI / X.length;
    time += dt;

    if (time > TWO_PI) {
      time = 0;
      path = [];
    }
  }
}