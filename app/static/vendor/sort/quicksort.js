function quickSort(arr, left, right,composite){
   var len = arr.length,
   pivot,
   partitionIndex;


  if(left < right){
    pivot = right;
    partitionIndex = partition(arr, pivot, left, right,composite);

   //sort left and right
   quickSort(arr, left, partitionIndex - 1,composite);
   quickSort(arr, partitionIndex + 1, right,composite);
  }
  return arr;
}

var partition=function (arr, pivot, left, right,composite){
   var pivotValue = arr[pivot],
       partitionIndex = left;

   for(var i = left; i < right; i++){
    if(composite(arr[i] , pivotValue)>0){
      swap(arr, i, partitionIndex);
      partitionIndex++;
    }
  }
  swap(arr, right, partitionIndex);
  return partitionIndex;
}
var swap=function (arr, i, j){
   var temp = arr[i];
   arr[i] = arr[j];
   arr[j] = temp;
}

