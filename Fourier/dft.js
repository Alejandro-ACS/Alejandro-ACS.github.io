function dft(x){
    let fourier = [];
    let pi = Math.PI;
    let N = x.length;
    for (let k = 0; k < N; k++){
        let re = 0;
        let im = 0;
        for (let n = 0; n < N; n++){
            re += x[n][0]*Math.cos(2*pi*k*n/N)+x[n][1]*Math.sin(2*pi*k*n/N);
            im += x[n][0]*(-Math.sin(2*pi*k*n/N))+x[n][1]*Math.cos(2*pi*k*n/N);
        }
        re = re/N;
        im = im/N;

        let freq = k;
        let amp = Math.sqrt(re*re+im*im);
        let phase = Math.atan2(im, re);

        fourier[k] = {re, im, freq, amp, phase};
    }
    return fourier;
}