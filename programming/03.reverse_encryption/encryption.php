<?php

    function evalCrossTotal($strMD5){
        $intTotal = 0;
        $arrMD5Chars = str_split($strMD5, 1);
        foreach ($arrMD5Chars as $value)
        {
            $intTotal += '0x0'.$value;
        }
        return $intTotal;
    }


    function encryptString($strString, $strPassword){
        // $strString is the content of the entire file with serials
        $strPasswordMD5 = md5($strPassword);
        $intMD5Total = evalCrossTotal($strPasswordMD5);
        $arrEncryptedValues = array();
        $intStrlen = strlen($strString);
        for ($i=0; $i<$intStrlen; $i++)
        {
            $arrEncryptedValues[] =  ord(substr($strString, $i, 1))
                                  +  ('0x0' . substr($strPasswordMD5, $i%32, 1))
                                  -  $intMD5Total;
            $intMD5Total = evalCrossTotal(substr(md5(substr($strString,0,$i+1)), 0, 16)
                         .  substr(md5($intMD5Total), 0, 16));
        }
        return implode(' ' , $arrEncryptedValues);
    }
?> 
