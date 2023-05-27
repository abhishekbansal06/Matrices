M=matrix([[a,0],[c,a]])
M1=(matrix([[1,0],[t,1]])*M*matrix([[1,0],[-t,1]])).evalm()
print "Parabolic matrices: %s and  %s" % (M, M1)
print "%s (%s %s %s)" % (bool(M.op(0)-M.op(3)-M1.op(0)+M1.op(3)==0 and\
M.op(1)-M1.op(1)==0 and M.op(2)-M1.op(2)==0),\
M.op(0)-M.op(3)-M1.op(0)+M1.op(3)==0, \
M.op(1)-M1.op(1)==0, M.op(2)-M1.op(2)==0)
print "Parabolic inner product: %s" % (matrix([[1,-x]])*M*matrix([[y],[1]])).evalm().op(0).normal()
print "Quadratic form: %s" % (matrix([[1,-x]])*M*matrix([[x],[1]])).evalm().op(0).normal()
print

M=matrix([[a,-b],[b,a]])
M1=(matrix([[cos(t),sin(t)],[-sin(t),cos(t)]])*M*matrix([[cos(t),-sin(t)],[sin(t),cos(t)]])).evalm().normal()\
.subs(cos(t)*sin(t)==sin(2*t)/2,subs_options.subs_algebraic)\
.subs(pow(sin(t),2)==1-pow(cos(t),2),subs_options.subs_algebraic).normal()
print "Elliptic maptices: %s and %s" % (M, M1)
print "%s (%s %s %s)" % (bool(M.op(0)-M.op(3)-M1.op(0)+M1.op(3)==0 and\
M.op(1)-M1.op(1)==0 and M.op(2)-M1.op(2)==0),\
M.op(0)-M.op(3)-M1.op(0)+M1.op(3)==0, \
M.op(1)-M1.op(1)==0, M.op(2)-M1.op(2)==0)
print "Elliptic inner product: %s" % (matrix([[1,-x]])*M*matrix([[y],[1]])).evalm().op(0).normal()
print "Quadratic form: %s" % (matrix([[1,-x]])*M*matrix([[x],[1]])).evalm().op(0).normal()
print

M=matrix([[a,b],[b,a]])
M1=(matrix([[cosh(t),sinh(t)],[sinh(t),cosh(t)]])*M*matrix([[cosh(t),-sinh(t)],[-sinh(t),cosh(t)]])).evalm().normal()\
.subs(cosh(t)*sinh(t)==sin(2*t)/2,subs_options.subs_algebraic)\
.subs(pow(cosh(t),2)==1+pow(sinh(t),2),subs_options.subs_algebraic).normal()
print "Hyperbolic: %s and %s" % (M, M1)
print "%s (%s %s %s)" % (bool(M.op(0)-M.op(3)-M1.op(0)+M1.op(3)==0 and\
M.op(1)-M1.op(1)==0 and M.op(2)-M1.op(2)==0),\
M.op(0)-M.op(3)-M1.op(0)+M1.op(3)==0, \
M.op(1)-M1.op(1)==0, M.op(2)-M1.op(2)==0)
print "Hyperbolic inner product: %s" % (matrix([[1,-x]])*M*matrix([[y],[1]])).evalm().op(0).normal()
print "Quadratic form: %s" % (matrix([[1,-x]])*M*matrix([[x],[1]])).evalm().op(0).normal()
