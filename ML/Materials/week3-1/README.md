ps1.pdf에서 3번, 4번이 과제입니다. </br>
4번 먼저 푸시고 3번 푸시는걸 권해드립니다. </br>
3번 코딩 문제의 경우, ps1.zip에서 poisson 폴더를 열어서 작업하시면 되겠습니다. </br>
환경설정 및 프로그래밍에 어려움이 있으신 분들을 위해 저녁에 저번 WLS 때처럼 틀을 만들어놓은 파일을 추가로 업로드할 예정이니, 필요하신 분들은 이용해주시면 되겠습니다.</br>
-> 업로드했습니다. 원안인 ps1.zip이 아닌, 해당 파일을 이용하실 분들은 Poisson_regression.zip을 사용해주시면 되겠습니다. instruction은 아래와 같습니다.

[ by 조교 손재훈 ]

안녕하세요.
이번 Poisson regression 코딩 과제 업로드 했습니다. (Poisson_regression.zip)
src/poisson_regression에만 코드 작성하시고, main.py 실행해서 prediction 파일 저장 후 compare.py 파일 실행해서 구현한 모델과 sklearn의 poisson regression 모델을 비교해보시면 됩니다.

구현 완성 기준은 
1. 본인이 구현한 모델과 sklearn의 모델의 상대오차 평균이 0.03% 이하
2. max iteration 달성 시 또는 update 값 변화 거의 없는 경우 반복문을 종료
입니다.

추가적으로, /src/linear_model.py에서 max iteration을 수정할 수 있으니 편하게 조정하셔도 됩니다.

이번 과제는 난이도가 비교적 쉽기 때문에 다른 힌트를 두지 않았으나, 필요한 경우 추가하겠습니다.
감사합니다.

