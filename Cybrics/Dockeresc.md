It was a Simple Challenge.
An Image is given to you with the command they use to run their docker container

docker run --rm -it --detach-key=
"ctrl-p,p,i,c,t,u...."

Detach key is use to close the container safely, So challenge is to find the detach key

Its special feature is till the Correct detach key is entered by you in the terminal it won't show as the key is getting registered for detach funtion.
As soon as wrong key is pressed it will show you on the screen.

So basically it becomes simple bruteforce scenario in which you have to type different characters and check if they pop on the screen or not.

By doing this I got the full detach key that was :  "ctrl+P,p,i,c,t,u,r,e,i,s,w,o,r,t,h,a,t,h,o,u,s,a,n,d,w,o,r,d,s"

as soon as you type this message with ctf flag will pop up.
