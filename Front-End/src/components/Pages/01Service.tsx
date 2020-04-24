import React, { FunctionComponent, useState, useEffect, Component } from 'react';
import { StyledText, StyledBtn } from '../style';
import { Link } from 'react-router-dom';

// const goLogin: FunctionComponent<any> = () => {
  
// }

const Service: FunctionComponent<any> = ({ }) => {
  return (
    <>
      <StyledText id="myMenu">

        <h2>42000건의 빅데이터를 활용해<br />
        여러분의 소비를 비교/분석 해드려요.<br />
        식비 맞춤형 맛집도 추천해드립니다.<br />
        회원가입을 하면 더 많은 서비스를<br />
            이용하실 수 있어요</h2>
        <StyledBtn >
          <Link to="/loginPage">
            회원가입 하러가기
          </Link>
        </StyledBtn>
        <StyledBtn data-menuanchor="thirdPage">
          <a href="#thirdPage">그냥 볼래요</a>
        </StyledBtn>
      </StyledText>
    </>
  )
}



export default Service;