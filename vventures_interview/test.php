<?php

class StupidClassTest extends PHPUnit_Framework_TestCase  {
    
  public static function setUpBeforeClass() {
    $a = new StupidClass();
  }
  
  public function testDoNothing() {
    $b = $a->doNothing('Dayo');
    $this->assertEquals($b, 'Dayo');
  }
  
  public function testRepeatOnce()  {
    $c = $a->repeatOnce('Dayo');
    $this->assertEquals($c, 'DayoDayo');
  }

  public function testRepeatTwice() {
    $d = $a->repeatTwice('Dayo');
    $this->assertEquals($d, 'DayoDayoDayo');
  }

  /**
    * @expectedException InvalidArgumentException
    */
  public function testException() {
    $e = $a->doNothing();
  }

}

?>
