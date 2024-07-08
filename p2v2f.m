clear;
clc;
close all;
tic;
frame = 0;
videopath = ('.\practice2F\'); %in my current directory
%videopath = ('C:\Users\ehusse5\Downloads\ERSP\processing\practice1F');
mkdir('.\imagesP2\'); % creating the images folder

video = VideoReader([videopath 'practice2V.mp4']); % reading in each video
%video = VideoReader(videopath, );
while hasFrame(video) % reading in each video frame (until there is no more) to create that frame that into an image
    frame = frame+1;
    img = readFrame(video);
    if rem((frame-1), 1) == 0 % this may not be needed. If true also works
        imwrite(imresize(img, [1080 1920]), ['.\imagesP2\' num2str(frame) '.jpg']);
    end
end
toc;