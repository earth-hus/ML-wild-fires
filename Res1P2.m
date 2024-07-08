clear;
clc;
close all;
folder = '.\imagesP2\';
tic;
img_result = uint8(zeros(360*5, 360*8, 3));
for i = 1:7 % cereate the block of 5 by 8
    for j = 1 : 8
        img = imread([folder num2str(78+i*8+j) '.jpg']); % starts from image 369
        img_crop = img(120*3+(1:360), 60+180*2+(1:360), :); %changes the size
    %     img_crop = img(180*3+(1:360), :, :);
        img_result((i-1)*360+(1:360) , (j-1)*360+(1:360), :) = img_crop;
    end
end
imwrite(img_result, 'croppedP2.jpg');
%saves the orginal colored file

RGB = imread('croppedP2.jpg'); %grabs the orginal picture
%imshow(RGB)  % show original picture before grey


I = rgb2gray(RGB); % we use function to make it balck/white
%figure
%imshow(I) % show black and white picture

imwrite(I, 'bwCroppedP2.jpg'); % save in files
toc;