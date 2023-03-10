## 1. 柱状图
```Matlab
% # draw with Matlab
% 单列

x = 1:1:9;
y = [9, 36, 84, 126, 126, 84, 36, 9, 1];
b = bar(x,y,'FaceColor','flat');

d = listfonts;

xtips1 = b(1).XEndPoints;
ytips1 = b(1).YEndPoints;
labels1 = string(b(1).YData);
text(xtips1,ytips1,labels1,'HorizontalAlignment','center',...
    'VerticalAlignment','bottom','FontSize', 15);

b.EdgeColor = '#FFFFFF';
b.CData(1,:) = [161,217,155]/256;
b.CData(2,:) = [116,196,118]/256;
b.CData(3,:) = [65,171,93]/256;
b.CData(4,:) = [35,139,69]/256;
b.CData(5,:) = [35,139,69]/256;
b.CData(6,:) = [65,171,93]/256;
b.CData(7,:) = [116,196,118]/256;
b.CData(8,:) = [161,217,155]/256;
b.CData(9,:) = [199,233,192]/256;

set(gca,'FontSize',15);

title('Combination statistics', 'FontSize', 18)

txt1 = xlabel('Grid number', 'FontSize', 18);
% set(txt, 'Interpreter', 'latex');
% xlabel('Grid number $n$');
txt2 = ylabel('Number of feasible combinations', 'FontSize', 18);
% set(txt, 'Interpreter', 'latex');

ax = gcf;
exportgraphics(ax,'output/bar1.pdf','BackgroundColor','none');
% saveas(b, 'output/bar1.pdf')
```

```Matlab
% # draw with Matlab
% 双列

X = categorical({'W/O Defense','W/ LGS','W/ AT'});
X = reordercats(X,{'W/O Defense','W/ LGS','W/ AT'});
Y = [94.8 94.8 94.9; 43.0 46.2 91.6];

b = bar(X,Y,'FaceColor','flat');

d = listfonts;
xtips1 = b(1).XEndPoints;
ytips1 = b(1).YEndPoints;
labels1 = string(b(1).YData);
text(xtips1,ytips1,labels1,'HorizontalAlignment','center',...
    'VerticalAlignment','bottom','FontSize', 15);
xtips2 = b(2).XEndPoints;
ytips2 = b(2).YEndPoints;
labels2 = string(b(2).YData);
text(xtips2,ytips2,labels2,'HorizontalAlignment','center',...
    'VerticalAlignment','bottom','FontSize', 15);

b(1).EdgeColor = '#FFFFFF';
b(2).EdgeColor = '#FFFFFF';
b(1).CData(1,:) = [65,171,93]/256;
b(1).CData(2,:) = [65,171,93]/256;
b(1).CData(3,:) = [65,171,93]/256;
b(2).CData(1,:) = [255, 127, 127]/256;
b(2).CData(2,:) = [255, 127, 127]/256;
b(2).CData(3,:) = [255, 127, 127]/256;

set(gca,'FontSize',15);
title('Defense Evaluation', 'FontSize', 18);
txt1 = xlabel('Method', 'FontSize', 18);
txt2 = ylabel('AP (%)', 'FontSize', 18);

%set(b, {'DisplayName'}, {'W/O Attack','W/ Attack'}');
%legend();
lgd = legend('W/O Attack','W/ Attack');
lgd.Location = 'southwest';

ylim([0 110])

ax = gcf;
exportgraphics(ax,'output/bar2.pdf','BackgroundColor','none');

```

## 2. 折线图
```Matlab
% 折线图 + 图片

clear;clc
set(gcf,'position',[0 0 1100 700]);
% 确定整个图片的大小。250，300这两个参数不影响画布大小，其作用是确定画出来的图在电脑屏幕上的显示位置，改为0，0则图显示在电脑左下角。900，400确定画布宽高，900为宽，高400，画出的图为600x200的长方形。

t = tiledlayout(2,2,'TileSpacing','Compact','Padding','Compact');
nexttile

img1_path = 'test.jpg';
[X,img1_path] = imread(img1_path);
imshow(X,img1_path)

nexttile
x1 = [0    0.001001    0.002002    0.003003    0.004004    0.005005    0.006006    0.007007    0.008008    0.009009];
y1 = [1           1           1           1           1           1           1           1           1           1];
AP1 = 0.961;
p1 = plot(x1, y1);
p1.Color = [74/255,165/255,160/255];
p1.LineStyle = '-';
p1.LineWidth = 1.4;
hold on

x2 = [0    0.001001    0.002002    0.003003    0.004004    0.005005    0.006006    0.007007    0.008008    0.009009];
y2 = [1           1           1           1           1           1           1     0.92308     0.92308     0.92308];
AP2 = 0.743;
p2 = plot(x2, y2);
p2.Color = [221/255,149/255,91/255];
p2.LineStyle = '-';
p2.LineWidth = 1.4;

txt = 'w/o attack \rightarrow';
text(0.7, 0.9, txt, 'FontSize',14)

txt = 'w/ patch attack \rightarrow';
text(0.35, 0.7, txt, 'FontSize',14)
hold off

set(gca,'FontSize',14);  % 坐标轴刻度字体大小
ylim([0.0 1.02]);
xlim([0.0 1.02]);
legend('AP = 96.1%','AP = 74.3%', 'FontSize',14, 'Location','southwest');
title('Precision-Recall curve', 'FontSize',19)
xlabel('Recall', 'FontSize',17) 
ylabel('Precision', 'FontSize',17)

nexttile
img1_path = 'test.jpg';
[X,img1_path] = imread(img1_path);
imshow(X,img1_path)

nexttile
x1 = [0    0.001001    0.002002    0.003003    0.004004    0.005005    0.006006    0.007007];
y1 = [1           1           1           1           1           1           1           1];
AP1 = 0.937;
p1 = plot(x1, y1);
p1.Color = [74/255,165/255,160/255];
p1.LineStyle = '-';
p1.LineWidth = 1.4;
hold on

x2 = [0    0.001001    0.002002    0.003003    0.004004    0.005005    0.006006    0.007007    0.008008];
y2 = [1           1           1           1           1           1           1           1           1];
AP2 = 0.927;
p2 = plot(x2, y2);
p2.Color = [221/255,149/255,91/255];
p2.LineStyle = '-';
p2.LineWidth = 1.4;

x3 = [0    0.001001    0.002002    0.003003    0.004004    0.005005    0.006006    0.007007    0.008008];
y3 = [1           1           1           1           1           1           1           1           1];
AP3 = 0.610;
p3 = plot(x3, y3);
p3.Color = [192/255,0/255,0/255];
p3.LineStyle = '-';
p3.LineWidth = 1.4;

txt = 'w/o attack \rightarrow';
text(0.69, 0.79, txt, 'FontSize',14)

txt = 'w/ patch attack \rightarrow';
text(0.27, 0.92, txt, 'FontSize',14)

txt = 'w/ HALO attack \rightarrow';
text(0.3, 0.5, txt, 'FontSize',14)
hold off

set(gca,'FontSize',14);  % 坐标轴刻度字体大小
ylim([0.0 1.02]);
xlim([0.0 1.02]);
legend('AP = 93.7%','AP = 92.7%','AP = 61.0%', 'FontSize',14, 'Location','southwest');
title('Precision-Recall curve', 'FontSize',19)
xlabel('Recall', 'FontSize',17) 
ylabel('Precision', 'FontSize',17)

exportgraphics(t,'figures/test.pdf','BackgroundColor','none','ContentType','vector'); 
```