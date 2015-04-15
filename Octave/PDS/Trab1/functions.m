clc;

function y = shfft(a,m,N)
  if length(a) > N
	error('N must be >= the length of x')
  end
  a = [a zeros(1,N - length(a))];
  n = [0:N-1];
  n = mod(n - m,N);
  y = a(n+1);
endfunction

function y = circonv(x,h,N)
  if length(x) > N
	error('N must be >= the length of x');
  end
  if length(h) > N
	error('N must be >= the length of h');
  end
  x = [x zeros(1,N - length(x))];
  h = [h zeros(1,N - length(h))];
  m = 0:N-1;
  h = h(mod(-m,N)+1);
  H = zeros(N,N);
  for n = 1:N
	H(n,:) = shfft(h,n-1,N);
  end
  y = x*H';
endfunction
	  
