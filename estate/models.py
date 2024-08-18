from django.db import models

class AptTransaction(models.Model):
    sgg_cd = models.CharField(max_length=5)                                 # 법정동시군구코드
    umd_cd = models.CharField(max_length=5)                                 # 법정동읍면동코드
    land_cd = models.CharField(max_length=1, null=True, blank=True)         # 법정동지번코드
    bonbun = models.CharField(max_length=4, null=True, blank=True)          # 법정동본번코드
    bubun = models.CharField(max_length=4, null=True, blank=True)           # 법정동부번코드
    road_nm = models.CharField(max_length=100, null=True, blank=True)       # 도로명
    road_nm_sgg_cd = models.CharField(max_length=5, null=True, blank=True)  # 도로명시군구코드
    road_nm_cd = models.CharField(max_length=7, null=True, blank=True)      # 도로명코드
    road_nm_seq = models.CharField(max_length=2, null=True, blank=True)     # 도로명일련번호코드
    road_nmb_cd = models.CharField(max_length=1, null=True, blank=True)     # 도로명지상지하코드
    road_nm_bonbun = models.CharField(max_length=5, null=True, blank=True)  # 도로명건물본번호코드
    road_nm_bubun = models.CharField(max_length=5, null=True, blank=True)   # 도로명건물부번호코드
    umd_nm = models.CharField(max_length=60)                                # 법정동
    apt_nm = models.CharField(max_length=100)                               # 단지명
    jibun = models.CharField(max_length=20, null=True, blank=True)          # 지번
    exclu_use_ar = models.DecimalField(max_digits=22, decimal_places=4, null=True, blank=True)  # 전용면적
    deal_year = models.IntegerField()                                       # 계약년도
    deal_month = models.IntegerField()                                      # 계약월
    deal_day = models.IntegerField()                                        # 계약일
    deal_amount = models.CharField(max_length=40)                           # 거래금액(만원)
    floor = models.IntegerField(null=True, blank=True)                      # 층
    build_year = models.IntegerField(null=True, blank=True)                 # 건축년도
    apt_seq = models.CharField(max_length=20)                               # 단지 일련번호
    cdeal_type = models.CharField(max_length=1, null=True, blank=True)              # 해제여부
    cdeal_day = models.CharField(max_length=8, null=True, blank=True)               # 해제사유발생일
    dealing_gbn = models.CharField(max_length=10, null=True, blank=True)            # 거래유형
    estate_agent_sgg_nm = models.CharField(max_length=3000, null=True, blank=True)  # 중개사소재지 (시군구단위)
    rgst_date = models.CharField(max_length=8, null=True, blank=True)               # 등기일자
    apt_dong = models.CharField(max_length=400, null=True, blank=True)              # 아파트 동명
    sler_gbn = models.CharField(max_length=100, null=True, blank=True)              # 매도자 거래주체정보
    buyer_gbn = models.CharField(max_length=100, null=True, blank=True)             # 매수자 거래주체정보
    land_leasehold_gbn = models.CharField(max_length=1, null=True, blank=True)      # 토지임대부 아파트 여부

    def __str__(self):
        return f"{self.apt_nm} - {self.deal_year}/{self.deal_month}/{self.deal_day} - {self.deal_amount}만원"
