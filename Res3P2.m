clear;
clc;
close all;
folder = '.\imagesP2\';
tic;
img_result = uint8(zeros(360, 1, 3));
for i = 1:40
        img = imread([folder num2str(78+i) '.jpg']);
        img_crop = img(120*3+(1:360), 60+180*2+(1:360), :); % x smaller numbers - top of the picture
    %     img_crop = img(180*3+(1:360), :, :);
        img_result(: , (i-1)*10+(1:10), :) = img_crop(:, 176:185, :);
end
imwrite(img_result, 'vertical_linesP2.jpg');% saves the orginal colored file

RGB = imread('vertical_linesP2.jpg'); %grabs the orginal picture
%imshow(RGB)  % show original picture before grey


I = rgb2gray(RGB); % we use function to make it balck/white
%figure
%imshow(I) % show black and white picture

imwrite(I, 'bw_vertical_linesP2.jpg'); % save in files
toc;  