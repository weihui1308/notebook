## 1. 柱状图
```Matlab
% # draw with Matlab

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

```