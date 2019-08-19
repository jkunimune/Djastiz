hailyanoltulum = \relative {
	g'8 e'8 e8 d16 d8 c8 c16 c8 f8 f8 e8 e8( d16) c8 d8 e16 e8 d16( c16)
}
tepaltolon = \lyricmode {
	e a o i u yo la we na me ho co sa fe ko ta pe
}
\score{
	<<
		\new Voice = "" {
			\time 4/4
			\clef treble
			\hailyanoltulum
		}
		\new Lyrics \lyricsto "" {
			\tepaltolon
		}
	>>
}
