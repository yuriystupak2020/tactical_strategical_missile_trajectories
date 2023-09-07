% SCRIPT Glisada_Section_1_Module_2_Collision_Triangle.m performs the collision triangle
% calculations shown in Missile Guidance Fundamentals, Section_1_Module_2.
%
% This is a stand alone script.
%-------------------------------------------------------------------------------
VMVT = [0.5, 1 : 0.05 : 5]; nVMVT = length(VMVT);

L_rad = [0 : .01 : 40]*pi/180; nL = length(L_rad);

A_rad = zeros(nVMVT, nL);

for ii = 1 : nVMVT  
    for jj = 1 : nL  
        
        x = VMVT(ii)*sin(L_rad(jj));
        if abs(x) > 1
            A_rad(ii,jj) = NaN;
        else
            A_rad(ii,jj) = asin(x);
        end
        
    end  
end

contour(L_rad*180/pi, VMVT, A_rad*180/pi, [10:10:90]);
xlabel('Look Angle [deg]','fontsize',14);
ylabel('V_M/V_T', 'fontsize', 14);
title('Target Heading Angle [deg]','fontsize',14);
set(gca,'fontsize',14,'xlim',[0 40],'ylim',[1 5]);
set(gcf,'color','w');
grid on 
h = colorbar;
set(h,'fontsize',14);
