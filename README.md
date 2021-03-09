# hw1

一開始先Input.csv檔後再將C0A880, C0F9A0, C0G640, C0R190, C0X260這幾個station_id的抓出來，在這些資料中看TEMP適不適-99或-999，如果是就略過，如果不適就在跟上一次同一個staion_id的temp做比較並將
最大的留下，如果同一個staition_id裡全部的TEMP都是-99或-999就print none 否則就print出最大值的temp。
