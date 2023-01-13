w = [0:1:500]*pi/500
x = [1,-0.5,-0.3,-0.1]
y = zeros(1,length(w))
for i =1 : length(w)
   for n=-1 :2
       y(i) = y(i) + x(n+2)*exp(-j*w(i)*n);

   end
end

subplot (2,2,1);
plot(w/pi, real(y),"m");
xlabel("f");
ylabel('real');
subplot (2,2,2);
plot(w/pi, angle(y),"m");
xlabel("f");
ylabel ("Angel");
subplot(2,2,3);
plot(w/pi, imag(y),"m");
xlabel("f");
ylabel ("imaginary");
subplot(2,2,4);
plot (w/pi,abs(y),"m");
xlabel("f");
ylabel("Amplitude")