clc

n = 200;
close all
hold on
    color = [0, 0.4470, 0.7410;
        0.8500, 0.3250, 0.0980;
        0.9290, 0.6940, 0.1250;
        0.4660, 0.6740, 0.1880];


%     reward = table2array(rewards_no_noise);
%     reward = table2array(rewards_with_noise);
% reward = rewards_ddpg_with_noise;
reward = rewards_ddpg_50000;
%     reward = horzcat(table2array(rewards_no_noise), table2array(rewards_with_noise));
s = 0.1;    
    
for i=1:4
    raw = reward(i,:);
    avg = nanmean(reshape([raw; nan(mod(-numel(raw),n),1)],n,[]));
    std = nanstd(reshape([raw; nan(mod(-numel(raw),n),1)],n,[]));
    
    x = (1:1:numel(avg));
    patch([x fliplr(x)], [avg-s*std fliplr(avg+s*std)], color(i,:), 'EdgeColor', color(i,:), 'LineWidth', .1, 'FaceAlpha',.2, 'EdgeAlpha',.2)
%     plot(avg, 'Color', color(i,:), 'LineWidth', 1)

    
end

for i=1:4
    raw = reward(i,:);
    avg = nanmean(reshape([raw; nan(mod(-numel(raw),n),1)],n,[]));
    std = nanstd(reshape([raw; nan(mod(-numel(raw),n),1)],n,[]));
    
    x = (1:1:numel(avg));
%     patch([x fliplr(x)], [avg-std fliplr(avg+std)], color(i,:), 'EdgeColor', [1, 1, 1], 'FaceAlpha',.3)
    ax(i) = plot(avg, 'Color', color(i,:), 'LineWidth', 1);
    
end
legend(ax,'Agent 1 (Team A)','Agent 2 (Team A)','Agent 3 (Team B)','Agent 4 (Team B)')
xlabel(['Episode (\times' num2str(n) ')'])
ylabel('Reward')
grid on
% xline(100, '.');
