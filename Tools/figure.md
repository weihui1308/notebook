### 1. 柱状图
```python
# draw with python

import matplotlib.pyplot as plt
import numpy as np

name_list = ['GoogleAP', 'DPATCH', 'TextureAP', 'LAP', 'Ours']
num_list = [79.65, 93.11, 25.53, 43.07, 46.57]
num_list1 = [82.08, 97.91, 67.02, 83.32, 50.75]
x = list(range(len(num_list)))
x1 = np.arange(len(name_list))
total_width, n = 0.8, 2
width = total_width / n

#plt.xticks(rotation=20)
plt.xlabel("Adversarial patch", fontdict={'size': 14})  #设置X轴Y轴名称
plt.ylabel("Average precision (%)", fontdict={'size': 14})

for a, b in zip(x1, num_list):
    plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=9)
for a, b in zip(x1, num_list1):
    plt.text(a+0.4, b, '%.2f' % b, ha='center', va='bottom', fontsize=9)

plt.xticks(x1+0.2, labels=name_list)

plt.bar(x, num_list, width=width, label='W/O scaling', fc='#B0C4DE')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list1, width=width, label='W/ scaling', fc='#4682B4')
plt.legend()
#plt.show()
plt.tight_layout()
plt.savefig("zhuv1.pdf")
```

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