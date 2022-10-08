
function binarySearch(num, arr){
    let start = 0;
    let end = arr.length-1;

    while(start<=end){
        let middle = (start+end)/2;

        if(arr[middle]===num) return `${num} is present at index ${middle}`;

        if(arr[middle]>num) end = middle-1;
        else start = middle+1;

    }

    return `Not present in the array`;

}


let arr = [2,4,6,8,12,15,20,24,30,33,40,42,80];
const ans = binarySearch(8,arr);
console.log(ans);