import os
import requests
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from estate.models import AptTransaction
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = 'Fetch real estate data from the API and print the raw response'

    def handle(self, *args, **kwargs):
        url = "http://apis.data.go.kr/1613000/RTMSDataSvcAptTradeDev/getRTMSDataSvcAptTradeDev"
        params = {
            "LAWD_CD": "41590",
            "DEAL_YMD": "202402",
            "serviceKey": os.getenv('SERVICE_KEY'),
            "pageNo": "1",
            "numOfRows": "1"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            root = ET.fromstring(response.content)
            for item in root.findall('.//item'):
                AptTransaction.objects.create(
                    sgg_cd=item.find('sggCd').text,
                    umd_cd=item.find('umdCd').text,
                    land_cd=item.find('landCd').text if item.find('landCd') is not None else None,
                    bonbun=item.find('bonbun').text if item.find('bonbun') is not None else None,
                    bubun=item.find('bubun').text if item.find('bubun') is not None else None,
                    road_nm=item.find('roadNm').text if item.find('roadNm') is not None else None,
                    road_nm_sgg_cd=item.find('roadNmSggCd').text if item.find('roadNmSggCd') is not None else None,
                    road_nm_cd=item.find('roadNmCd').text if item.find('roadNmCd') is not None else None,
                    road_nm_seq=item.find('roadNmSeq').text if item.find('roadNmSeq') is not None else None,
                    road_nmb_cd=item.find('roadNmbCd').text if item.find('roadNmbCd') is not None else None,
                    road_nm_bonbun=item.find('roadNmBonbun').text if item.find('roadNmBonbun') is not None else None,
                    road_nm_bubun=item.find('roadNmBubun').text if item.find('roadNmBubun') is not None else None,
                    umd_nm=item.find('umdNm').text,
                    apt_nm=item.find('aptNm').text,
                    jibun=item.find('jibun').text if item.find('jibun') is not None else None,
                    exclu_use_ar=item.find('excluUseAr').text if item.find('excluUseAr') is not None else None,
                    deal_year=int(item.find('dealYear').text),
                    deal_month=int(item.find('dealMonth').text),
                    deal_day=int(item.find('dealDay').text),
                    deal_amount=item.find('dealAmount').text,
                    floor=int(item.find('floor').text) if item.find('floor') is not None else None,
                    build_year=int(item.find('buildYear').text) if item.find('buildYear') is not None else None,
                    apt_seq=item.find('aptSeq').text,
                    cdeal_type=item.find('cdealType').text if item.find('cdealType') is not None else None,
                    cdeal_day=item.find('cdealDay').text if item.find('cdealDay') is not None else None,
                    dealing_gbn=item.find('dealingGbn').text if item.find('dealingGbn') is not None else None,
                    estate_agent_sgg_nm=item.find('estateAgentSggNm').text if item.find('estateAgentSggNm') is not None else None,
                    rgst_date=item.find('rgstDate').text if item.find('rgstDate') is not None else None,
                    apt_dong=item.find('aptDong').text if item.find('aptDong') is not None else None,
                    sler_gbn=item.find('slerGbn').text if item.find('slerGbn') is not None else None,
                    buyer_gbn=item.find('buyerGbn').text if item.find('buyerGbn') is not None else None,
                    land_leasehold_gbn=item.find('landLeaseholdGbn').text if item.find('landLeaseholdGbn') is not None else None,
                )
            self.stdout.write(self.style.SUCCESS('Successfully fetched the data'))
        else:
            self.stdout.write(self.style.ERROR(f"Failed to fetch data: {response.status_code}"))
