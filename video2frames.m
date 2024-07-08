clear;
clc;
close all;
tic;
frame = 0;
videopath = ('.\continue\videos'); %in my current directory
mkdir('.\images'); % creating the images folder
for i = 1 : 8
    video = VideoReader([videopath '\Q' num2str(i) '.mp4']); % reading in each video
    while hasFrame(video) % reading in each video frame (until there is no more) to create that frame that into an image
        frame = frame+1;
        img = readFrame(video);
        if rem((frame-1), 1) == 0 % this may not be needed. If true also works
            imwrite(imresize(img, [1080 1920]), ['.\images\' num2str(frame) '.jpg']);
        end
    end
end
toc;