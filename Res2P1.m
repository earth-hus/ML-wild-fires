clear;
clc;
close all;
folder = '.\imagesP1\';
tic;
img_result = uint8(zeros(1, 360, 3));
for i = 1:40 % now we want to 
        img = imread([folder num2str(1292+i) '.jpg']);
        img_crop = img(180*3+(1:360), 15+180*2+(1:360), :);
    %     img_crop = img(180*3+(1:360), :, :);
        img_result((i-1)*10+(1:10) , :, :) = img_crop(176:185, :, :);
end
imwrite(img_result, 'horizontal_linesP1.jpg'); % saves the orginal colored file

RGB = imread('horizontal_linesP1.jpg'); %grabs the orginal picture
%imshow(RGB)  % show original picture before grey


I = rgb2gray(RGB); % we use function to make it balck/white
%figure
%imshow(I) % show black and white picture

imwrite(I, 'bw_horizontal_linesP1.jpg'); % save in files

toc;