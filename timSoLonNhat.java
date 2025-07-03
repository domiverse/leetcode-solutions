public class timSoLonNhat {

    /**
     * Hàm này tìm và trả về số lớn nhất trong một mảng số nguyên.
     * @param arr Mảng số nguyên đầu vào.
     * @return Số lớn nhất trong mảng.
     * @throws IllegalArgumentException nếu mảng rỗng hoặc null.
     */
    public static int timSoLonNhat(int[] arr) {
        if(arr == null || arr.length == 0){
            throw new IllegalArgumentException("mang dang bị null");
        }
        int soLonNhat = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if(arr[i] > soLonNhat){
                soLonNhat = arr[i] ;
            }
        }
            return soLonNhat;
    }


    public static void main(String[] args) {
        int[] mangSo = {15, 8, 99, 42, 7, 101, 3};
        int ketQua = timSoLonNhat(mangSo);
        System.out.println("Số lớn nhất trong mảng là: " + ketQua); // Kết quả: 101s
        
    }
}