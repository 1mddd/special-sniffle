%%一致性检验
function f =consistent(a)

[~,y]=eig(a);
ci=(max(max(y))-size(a,1))./(size(a,1))-1
ri=[0 0.0001 0.52 0.89 1.12 1.26 1.36 1.41 1.46 1.49 1.52 1.54 1.56 1.58 1.59];
cr=ci./ri(size(a,1))

if cr<0.1
    f=1;
else
    f=0;
end
end


