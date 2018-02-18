The mat-files digits-train and digits-test contain training and testing data for the "digits" dataset. 

digits-{train, test}.mat contains:

images_{train, test}: 784 x 5000 double containing vectorized images in its columns. In matlab, you can view the image in the first column by the following command
imshow(reshape(images_train(:, 1), 28, 28))

labels_{train, test}: 5000 x 1 uint8 containing image labels 1,2,3,4,5 (for training) and 6,7,8,9,10 (for testing) corresponding to different digits. Note that labels_test is not provided to you and is held out for evaluation purposes.

fea_hog_{train, test}: 496 x 5000 double containing vectorized HOG features [1] computed with the vl_feat toolbox [2].

fea_scat_{train, test}: 3472 x 5000 double containing vectorized features extracted from scattering convolutional network [3].

[1] P. F. Felzenszwalb, R. B. Grishick, D. McAllester, and D. Ramanan. Object detection with discriminatively trained part based models. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2009.
[2] A. Vedaldi and B. Fulkerson. VLFeat: An open and portable library of computer vision algorithms. http://www.vlfeat.org/, 2008.
[3] J. Bruna and S. Mallat. Invariant scattering convolution networks. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2013.