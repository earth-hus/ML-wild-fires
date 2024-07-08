clear;
clc;
close all;
folder = '.\images\';
tic;
img_result = uint8(zeros(1, 360, 3));
for i = 1:40 % now we want to 
        img = imread([folder num2str(659+i) '.jpg']);
        img_crop = img(180*3+(1:360), 60+180*2+(1:360), :);
    %     img_crop = img(180*3+(1:360), :, :);
        img_result((i-1)*10+(1:10) , :, :) = img_crop(176:185, :, :);
end
imwrite(img_result, 'horizontal_lines.jpg'); % saves the orginal colored file

RGB = imread('horizontal_lines.jpg'); %grabs the orginal picture
%imshow(RGB)  % show original picture before grey


I = rgb2gray(RGB); % we use function to make it balck/white
%figure
%imshow(I) % show black and white picture

imwrite(I, 'bw_horizontal_lines.jpg'); % save in files

toc;